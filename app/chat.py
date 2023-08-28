import requests
import time


while True:
    time.sleep(20)
    response = requests.get('http://127.0.0.1:8000/api/v1/rooms/1').json()
    print(response['messages'])
    