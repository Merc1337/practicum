

**Задания для выполнения**
На основе предложенного шаблона реализуйте сервис, реализующий регистрацию пользователей. Сервис должен поддерживать REST API и коллекцию /user/, хранящую данные о логинах и паролях пользователей, зарегистрированных в системе. Сервис должен принимать и отдавать информацию в формате JSON. Сервис должен хранить следующую информацию про каждого пользователя: логин, хеш пароля (лучше с солью), дату регистрации.


![image](https://user-images.githubusercontent.com/51966929/146623111-a4d1bb24-81a0-4bcf-a5a5-c22782c373cf.png)

![image](https://user-images.githubusercontent.com/51966929/146623119-9d40ad1a-9ca0-4552-9328-48d243865a72.png)

Хэширование:

![image](https://user-images.githubusercontent.com/51966929/146623129-b4ab33fd-08a6-4934-ba9a-d5cb46139d7c.png)

Информация о пользователях:

![image](https://user-images.githubusercontent.com/51966929/146623152-92548f50-40b4-4805-a635-bbfdad268511.png)


Настройте веб-сервер по Вашему выбору (Apache2 или nginx) таким образом, чтобы он поддерживал соединение по протоколу HTTPS. Для этого сгенирируйте самоподписанный сертификат SSL. Был сгенерирован самоподписанный ssl


![изображение](https://user-images.githubusercontent.com/51966929/146633708-2e5da715-36b3-4178-b805-0ea756793ba3.png)
