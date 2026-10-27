import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

dados = response.json()

for usuario in dados:
    print(usuario["name"], "-", usuario["email"])