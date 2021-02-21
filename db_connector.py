from flask import Flask, request
import pymysql

host, port, user, passwd, db = 'remotemysql.com', 3306, '9hkyb0ebUg', 'Q9XsNQ9fQw', '9hkyb0ebUg'

def insert(user_id, user_name):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()

        cursor.execute(f"INSERT into 9hkyb0ebUg.users (user_id, user_name, creation_date) VALUES ({user_id},'{user_name}', CURRENT_TIMESTAMP);")

        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(e)
        raise Exception

def select(user_id):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM 9hkyb0ebUg.users WHERE user_id = '{user_id}';")
        data = cursor.fetchall()
        user_name = data[0]['user_name']

        cursor.close()
        conn.close()
        return user_name
    except Exception as e:
        print(e)
        raise Exception

def update(user_id, user_name):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()

        cursor.execute(f"UPDATE 9hkyb0ebUg.users SET user_name = {user_name} WHERE user_id = '{user_id}';")

        cursor.close()
        conn.close()
        return user_name
    except Exception as e:
        print(e)
        raise Exception

def delete(user_id):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM 9hkyb0ebUg.users WHERE user_id = {user_id};")

        cursor.close()
        conn.close()
        return user_id
    except Exception as e:
        print(e)
        raise Exception


#cursor.close()
#conn.close()

#
# host='remotemysql.com'
# port=3306
# user='9hkyb0ebUg'
# passwd='Q9XsNQ9fQw'
# db='9hkyb0ebUg'

#
# def Insert(id, name):
#     # Establishing a connection to DB
#     conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
#     conn.autocommit(True)
#     # Getting a cursor from Database
#     cursor = conn.cursor()
#     # Inserting data into table
#     try:
#         return cursor.execute(f"INSERT into 9hkyb0ebUg.users (user_id, user_name, creation_date) VALUES ({id},'{name}', CURRENT_TIMESTAMP);")
#     except Exception as e:
#         #db.rollback()
#         raise Exception(e.message)
#     finally:
#         cursor.close()
#         conn.close()
#
# def Update(id, name):
#     # Establishing a connection to DB
#     conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
#     conn.autocommit(True)
#     # Getting a cursor from Database
#     cursor = conn.cursor()
#     # Updating data in the table
#     try:
#         return cursor.execute(f"UPDATE 9hkyb0ebUg.users SET user_id = {id} WHERE user_name = '{name}';")
#     except Exception as e:
#         # db.rollback()
#         raise Exception(e.message)
#     finally:
#         cursor.close()
#         conn.close()
#
# def Delete(id):
#     # Establishing a connection to DB
#     conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
#     conn.autocommit(True)
#     # Getting a cursor from Database
#     cursor = conn.cursor()
#     # Deleting data from table
#     try:
#         return cursor.execute(f"DELETE FROM 9hkyb0ebUg.users WHERE user_id = {id};")
#     except Exception as e:
#         # db.rollback()
#         raise Exception(e.message)
#     finally:
#         cursor.close()
#         conn.close()
#
# def GetByID(id):
#     # Establishing a connection to DB
#     conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
#     conn.autocommit(True)
#     # Getting a cursor from Database
#     cursor = conn.cursor()
#     # Getting a data by id
#     try:
#         return cursor.execute(f"SELECT * FROM 9hkyb0ebUg.users WHERE user_id = {id};")
#     except Exception as e:
#         # db.rollback()
#         raise Exception(e.message)
#     finally:
#         cursor.close()
#         conn.close()
#
# def Get():
#     # Establishing a connection to DB
#     conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
#     conn.autocommit(True)
#     # Getting a cursor from Database
#     cursor = conn.cursor()
#     # Getting all data from table “users”
#     try:
#         return cursor.execute("SELECT * FROM 9hkyb0ebUg.users;")
#     except Exception as e:
#         # db.rollback()
#         raise Exception(e.message)
#     finally:
#         cursor.close()
#         conn.close()

# # Iterating table and printing all users
# for row in cursor:
#     print(row)

#cursor.close()
#conn.close()1