import requests

# stop rest app
try:
    requests.get('http://127.0.0.1:5000/stop_server')
except Exception:
    pass
finally:
    print("stop rest app")

# stop web app
try:
    requests.get('http://127.0.0.1:5001/stop_server')
except Exception:
    pass
finally:
    print("stop web app")

