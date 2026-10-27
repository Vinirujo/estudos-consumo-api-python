
import requests

id_usuario = input("Digite o ID do usuário que deseja excluir: ")

url = f"https://jsonplaceholder.typicode.com/users/{id_usuario}"

confirmacao = input(f"Tem certeza que deseja excluir o usuário {id_usuario}? (S/N): ").strip().upper()

if confirmacao == "S":
    try:
        response = requests.delete(url, timeout=5)

        if response.status_code in (200, 204):
            print("Solicitação de exclusão realizada com sucesso!")

        else:
            print("Não foi possível excluir o usuário.")
            print(f"Status code: {response.status_code}")

    except requests.exceptions.RequestException as erro:
        print("Não foi possível acessar a API.")
        print(f"Erro: {erro}")

else:
    print("Exclusão cancelada pelo usuário.")