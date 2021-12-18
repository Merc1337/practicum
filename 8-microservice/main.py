import flask
import csv
from datetime import datetime
from flask import Flask, request
from hashlib import sha256
import string
import random


filename = 'database.txt'
app = Flask(__name__)


def hasher(password, salt=None):
    if salt == None:
        letters_and_digits = string.ascii_letters + string.digits
        salt = ''.join(random.sample(letters_and_digits, 16))
        salt = salt.encode('utf-8')
    # salt = os.urandom(16).decode('utf-8')
    password = sha256((password).encode('utf-8') + salt).hexdigest()
    return salt, password




def save_user(requester, filename):
    email, passwd = requester['email'], requester['password']
    reg_date = datetime.now().strftime("%Y%m%d", "%H:%M:%S")
    password = hasher(passwd)
    line = [email, password, reg_date]
    with open(filename,'a') as file:
            file.writelines(line)


def request_info(result=True, description="", exception=None):
    info = {
        "result": result,
        "description": description,
        "exception": exception
    }
    return info

def authentification(requester):
    email = requester['email']
    password = requester['password']
    with open(filename,'r') as file:
        lines=file.readlines()
        for line in lines:
                if email not in line:
                        return request_info(True, 'User does not exist')
                else:
                    passwd=line[1]
                    test_pass=hasher(password,passwd)
                        if passwd==test_pass:
                            return request_info(True, 'authentificated')
                        else: return request_info(False, 'invalid password', 'password error')



@app.route('/user/user_auth', methods=['POST'])
def user_auth():
    requester = request.get_json()
    return authentification(requester)


@app.route('/user/user_register', methods=['POST'])
def user_register():
    requester = request.get_json()
    save_user(requester)

    return request_info(True, 'registration has been done')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)