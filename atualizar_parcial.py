
import requests

id_usuario = input("Digite o ID do usuário: ")

url = f"https://jsonplaceholder.typicode.com/users/{id_usuario}"

alteracoes = {
    "email": input("Digite o novo email: ")
}

try:
    response = requests.patch(url, json=alteracoes, timeout=5)

    if response.status_code == 200:
        dados = response.json()

        print("\nUsuário atualizado com sucesso!")
        print(f"ID: {dados['id']}")
        print(f"Nome: {dados['name']}")
        print(f"Email: {dados['email']}")

    else:
        print("Não foi possível atualizar o usuário.")
        print(f"Status code: {response.status_code}")

except requests.exceptions.RequestException as erro:
    print("Não foi possível acessar a API.")
    print(f"Erro: {erro}")
