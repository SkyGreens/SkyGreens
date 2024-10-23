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
    
    url = "http://localhost:8080/skygreen/fornecedor/adicionar"

    data = {
        "ativo" : "true",
        "email" : "teste4@gmail.com",
        "telefone" : "12988545461",
        "endereco" : "Rua santa cruz",
        "cidade" : "Jacarei",
        "estado" : "SP",
        "pais" : "Brasil",
        "inscricaoEstadual" : "132458752",
        "razaoSocial" : "Sky Green",
        "cnpj" : "03106082000303"
    }

    headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {token}"}
    
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print('Requisição bem-sucedida!')
        print('Resposta:', response.status_code)
    else:
        print('Falha na requisição. Código de status:', response.status_code)
else:
    print("Falha no login:", response.status_code)