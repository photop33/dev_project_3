import requests

id = 2

try:
    res = requests.get(f'http://127.0.0.1:5000/users/{id}')
    print("get response -", res.json())
    print("Testing docker_backend PASSED...")
    
except Exception as e:
    print("Testing docker_backend FAILED...")
    raise Exception(e)
