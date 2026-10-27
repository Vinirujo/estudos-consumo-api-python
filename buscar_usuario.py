import requests

input_id = input("Coloque o ID do usuario que deseja buscar: ")

url = f"https://jsonplaceholder.typicode.com/users/{input_id}"

try:
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        usuario = response.json()
        
        print("Usuario encontradocom sucesso:")
        print(f"Nome: {usuario['name']}")
        print(f"Email: {usuario['email']}")
    
    elif response.status_code == 404:
        print("Usuario não encontrado.")
        
    else:
        print(f"Erro ao buscar usuario.") 
        print(f"Código de status: {response.status_code}")

except requests.exceptions.RequestException as erro: 
    print("Não foi possível acessar a API")
    print(f"Erro: {erro}")