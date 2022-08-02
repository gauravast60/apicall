import requests


response = requests.get('http://127.0.0.1:5000/app/api/courses/all')
print(response.status_code)
print(response.json())