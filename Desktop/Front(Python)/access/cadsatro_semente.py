import requests

# URL para login
url_login = "http://localhost:8080/skygreen/auth/login"

# Dados para login
login_data = {
    "cpf": "12345678909",
    "senha": "admin"
}

# Realiza o login
response = requests.post(url_login, json=login_data)

if response.status_code == 200:
    # Obtém o token JWT
    token = response.json().get("token")
    print(f"Token JWT recebido: {token}")

    # URL para cadastro da semente
    url_adicionar_semente = "http://localhost:8080/skygreen/sementes/adicionar"

    # Dados da semente a ser cadastrada
    semente_data = {
        "nome": "Semente de Alface",
        "descricao": "Semente ideal para cultivo hidropônico"
        #"nome": "Semente de Milho",
        #"descricao": "Semente ideal para cultivo hidropônico"
        
    }

    # Cabeçalho com o token de autenticação
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Faz o cadastro da semente
    response_semente = requests.post(url_adicionar_semente, json=semente_data, headers=headers)

    if response_semente.status_code == 200:
        print('Semente cadastrada com sucesso!')
        print("Dados recebidos:", response_semente.json())
    else:
        print('Falha ao cadastrar a semente:', response_semente.status_code)
        print('Resposta:', response_semente.text)  # Adicionado para depuração

else:
    print("Falha no login:", response.status_code)
