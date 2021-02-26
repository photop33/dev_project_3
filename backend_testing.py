import requests
import pymysql


id, user_name = 12, "dan12"

host, port, sqlPort, user, passwd, db = '127.0.0.1', 5000, 3306, 'root', '123456', 'db'

    
try:
    res = requests.post(f'http://{host}:{port}/users/{id}', json={"user_name": f'{user_name}'})
    print("post response -", res.json())

    res = requests.get(f'http://{host}:{port}/users/{id}')
    print("get response -", res.json())

except Exception as e:
    print("test failed",e)
    raise Exception(e)