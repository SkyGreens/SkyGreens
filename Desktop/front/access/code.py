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


    url_protegida = "http://localhost:8080/skygreen/usuario/listar"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response_protegida = requests.get(url_protegida, headers=headers)

    if response_protegida.status_code == 200:
        print("Acesso à rota protegida com sucesso!")
        print("Dados recebidos:", response_protegida.json())
    else:
        print("Falha ao acessar a rota protegida:", response_protegida.status_code)
else:
    print("Falha no login:", response.status_code)