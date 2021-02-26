import pymysql


host, port, user, passwd, db = 'mysql-db', 3306, 'root', '123456', 'db'

def insert(user_id, user_name):
    print("start insert", flush=True)
    # Establishing a connection to DB 
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    cursor.execute(f"INSERT into {db}.users (user_id, user_name, creation_date) VALUES ({user_id},'{user_name}', CURRENT_TIMESTAMP);")
        
    cursor.close()
    conn.close()
    return True
        

def select(user_id):
    print("start select", flush=True)
    # Establishing a connection to DB
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT * FROM {db}.users WHERE user_id = {user_id};")
    data = cursor.fetchall()
    user_name = data[0]['user_name']

    cursor.close()
    conn.close()
    return user_name

def update(user_id, user_name):
    print("start update")
    # Establishing a connection to DB
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {db}.users SET user_name = {user_name} WHERE user_id = {user_id};")

    cursor.close()
    conn.close()
    return user_name    
    

def delete(user_id):

    print("start delete")
    # Establishing a connection to DB
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {db}.users WHERE user_id = {user_id};")

    cursor.close()
    conn.close()
    return user_id
