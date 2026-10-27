
import requests

id_usuario = input("Digite o ID do usuário que deseja atualizar: ")

url = f"https://jsonplaceholder.typicode.com/users/{id_usuario}"

usuario_atualizado = {
    "name": input("Digite o novo nome: "),
    "username": input("Digite o novo username: "),
    "email": input("Digite o novo email: ")
}

try:
    response = requests.put(url, json=usuario_atualizado, timeout=5)

    if response.status_code == 200:
        dados = response.json()

        print("\nUsuário atualizado com sucesso!")
        print(f"ID: {dados['id']}")
        print(f"Nome: {dados['name']}")
        print(f"Username: {dados['username']}")
        print(f"Email: {dados['email']}")

    else:
        print("Não foi possível atualizar o usuário.")
        print(f"Status code: {response.status_code}")

except requests.exceptions.RequestException as erro:
    print("Não foi possível acessar a API.")
    print(f"Erro: {erro}")
