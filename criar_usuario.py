import requests


url = "https://jsonplaceholder.typicode.com/users/"

novo_usuario = {
    "name": input("Digite o nome: "),
    "username": input("Digite o nome de usuário: "),
    "email": input("Digite o email do usuário: ")
}

try:
    response = requests.post(url, json=novo_usuario, timeout=5)
    
    if response.status_code == 201:
        print("Usuário criado com sucesso!")

        usuario_criado = response.json()
        print(f"ID: {usuario_criado['id']}")
        print(f"Nome: {usuario_criado['name']}")
        print(f"Username: {usuario_criado['username']}")
        print(f"Email: {usuario_criado['email']}")
        
    else:
        print("Erro ao buscar usuario.") 
        print(f"Código de status: {response.status_code}")

except requests.exceptions.RequestException as erro: 
    print("Não foi possível acessar a API")
    print(f"Erro: {erro}")