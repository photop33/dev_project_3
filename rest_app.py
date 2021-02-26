from flask import Flask, request
from db_connector import insert, select, update, delete
import os
import signal
import pymysql

app = Flask(__name__)

# Use CRUD ops on users table
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def users(user_id):
    if request.method == 'POST':
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            insert(user_id, user_name)
            return {'status': 'ok', 'user_added': user_name}, 200 # status code
        except pymysql.err.IntegrityError as ie:
            print("Duplicate entry for PRIMARY key",ie)        
            return {'status': 'error', 'reason': 'id already exists'}, 500
        except ( RuntimeError, pymysql.err.OperationalError ) as oe:
            print("Can't connect to MySQL server", oe)
            return {'status': 'error', 'reason': "Can't connect to MySQL server"}, 500
        except Exception as e:
            print("Unknown error",e)    
            return {'status': 'error', 'reason': 'unknown'}, 500
            
    elif request.method == 'GET':
        try:
            user_name = select(user_id)
            return {'status': 'ok', 'user_name': user_name}, 200  # status code
        except IndexError as ie:
            print("No such id", ie)
            return {'status': 'error', 'reason': 'no such id'}, 500
        except Exception as e:
            print("Unknown error",e)    
            return {'status': 'error', 'reason': "Can't connect to MySQL server"}, 500
    elif request.method == 'PUT':
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            update(user_id, user_name)
            return {'status': 'ok', 'user_updated': user_name}, 200  # status code
        except IndexError as ie:
            print("No such id", ie)
            return {'status': 'error', 'reason': 'no such id'}, 500
        except Exception as e:
            print("Unknown error",e)    
            return {'status': 'error', 'reason': "Can't connect to MySQL server"}, 500
    elif request.method == 'DELETE':
        try:
            delete(user_id)
            return {'status': 'ok', 'user_deleted': user_id}, 200  # status code
        except IndexError as ie:
            print("No such id", ie)
            return {'status': 'error', 'reason': 'no such id'}, 500
        except Exception as e:
            print("Unknown error",e)    
            return {'status': 'error', 'reason': "Can't connect to MySQL server"}, 500


# Stop the server with http request
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


# Home page
@app.route('/')
def home():
    return 'Welcome to the flask server within docker, ' \
           'you can go to "/users/user_id" to search a user in database.'


app.run(host='0.0.0.0', debug=True, port=5000)