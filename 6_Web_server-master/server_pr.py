import socket
from threading import Thread
import time
import re
import json
from os.path import sep, isfile


def log(date, ip, filename, code):
    with open('logs.txt', 'a') as file:
        file.write('\n'.join([date, ip, filename, code, '\n']))


def get_date():
    t = time.asctime(time.gmtime()).split(' ')
    t = f'{t[0]}, {t[2]} {t[1]} {t[4]} {t[3]} GMT'
    return t


def code(path):
    if not isfile(path):
        return "Not Found"
    elif not re.findall(r'\.html|\.js|\.css|\.png', path):
        return "Forbidden"
    else:
        return "OK"


def path(request):
    if request == '/':
        return dic["dir"] + sep + 'index.html'
    else:
        return dic["dir"] + sep + request[1:].replace('/', sep)


def get_answer(request, addr):
    this_path = path(request)
    this_code = code(this_path)
    requested_file = this_path.split(sep)[-1]
    extension = this_path.split(".")[-1] if this_code == "OK" else "html"
    current_date = get_date()
    log(current_date, str(addr[0]),
              requested_file, str(dic[this_code]))
    answer = open(this_path, 'rb').read() if this_code == "OK" else "".encode()
    print(dic["sample"].format(dic[this_code], this_code, current_date,
                               dic[extension], len(answer)))
    return dic["sample"].format(dic[this_code], this_code, current_date,
                                dic[extension], len(answer)).encode() + answer


def enable(conn, addr):
    user_answer = conn.recv(dic["max_byte"]).decode()
    print(user_answer)
    request = user_answer.split(" ")[1]
    conn.send(get_answer(request, addr))


def create_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(('', dic["port"]))
            print(f"Using port {dic['port']}")
        except:
            sock.bind(('', dic["second_port"]))
            print(f"Using port {dic['second_port']}")
        sock.listen(5)
        while True:
            conn, addr = sock.accept()
            thread = Thread(target=enable, args=(conn, addr))
            thread.start()
            print("Connected", addr)
    except KeyboardInterrupt:
        sock.close()
        print('Server is closed...')


if __name__ == "__main__":
    dic = {}
    with open('settings.json', 'r') as file:
        dic = json.load(file)
    create_socket()
