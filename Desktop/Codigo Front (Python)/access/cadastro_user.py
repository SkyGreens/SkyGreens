import requests

url_login = "http://localhost:8080/skygreen/auth/login"

login_data = {
    "cpf": "12345678909",
    "senha": "admin"
}

response = requests.post(url_login, json=login_data)

if response.status_code == 200:
    
    token = response.json().get("token")
    print(f"Token JWT recebido: {token}")
    
    url = 'http://localhost:8080/skygreen/auth/register'

    # Dados a serem enviados no corpo da requisição
    data = {
        "cpf" : "48983452803",
        "senha" : "489",
        "role" : "GERENTEPRODUCAO",
        "nome" : "Cauane",
        "ativo" : "true",
        "email" : "teste3@gmail.com"
    }

    headers = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {token}"
    }
    # Fazer a requisição POST
    response = requests.post(url, json=data, headers=headers)

    # Verificar a resposta
    if response.status_code == 200:
        print('Requisição bem-sucedida!')
        print('Resposta:', response.status_code)
    else:
        print('Falha na requisição. Código de status:', response.status_code)
else:
    print("Falha no login:", response.status_code)