
import requests

url = "https://jsonplaceholder.typicode.com/users"

username = input("Digite o username que deseja buscar: ")

parametros = {
    "username": username
}

try:
    response = requests.get(
        url,
        params=parametros,
        timeout=5
    )

    if response.status_code == 200:
        usuarios = response.json()

        if usuarios:
            for usuario in usuarios:
                print("\nUsuário encontrado!")
                print(f"ID: {usuario['id']}")
                print(f"Nome: {usuario['name']}")
                print(f"Username: {usuario['username']}")
                print(f"Email: {usuario['email']}")
        else:
            print("Nenhum usuário encontrado.")

    else:
        print("Erro na requisição.")
        print(f"Status code: {response.status_code}")

except requests.exceptions.RequestException as erro:
    print("Não foi possível acessar a API.")
    print(f"Erro: {erro}")
