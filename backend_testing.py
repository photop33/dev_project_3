import requests
import pymysql

id = 1818
user_name = "my Name"

try:
    res = requests.post(f'http://127.0.0.1:5000/users/{id}', json={"user_name": f'{user_name}'})
    print("post -", res.json())

    res = requests.get(f'http://127.0.0.1:5000/users/{id}')
    print("get -", res.json())

    host, port, user, passwd, db = 'remotemysql.com', 3306, '9hkyb0ebUg', 'Q9XsNQ9fQw', '9hkyb0ebUg'
    # Establishing a connection to DB
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, cursorclass=pymysql.cursors.DictCursor)
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM 9hkyb0ebUg.users WHERE user_id = {id};")
    data = cursor.fetchall()
    user_name = data[0]['user_name']
    print("DB -", user_name)
except Exception as e:
    raise Exception("test failed")