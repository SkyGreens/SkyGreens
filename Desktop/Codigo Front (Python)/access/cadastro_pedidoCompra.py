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
    
    # Cadastro do pedido de compra
    url_pedido = "http://localhost:8080/skygreen/compras/pedido"

    pedido_data = {
        "fornecedor": {
            "fornecedorId": 1
        },
        "pedidoCompraId": 0,
        "quantidade": 10,
        "semente": {
            "sementeId": 1
        }
    }

    headers = {'Content-Type': 'application/json', "Authorization": f"Bearer {token}"}
    
    response = requests.post(url_pedido, json=pedido_data, headers=headers)

    if response.status_code == 200:
        print('Pedido cadastrado com sucesso!')
    else:
        print('Falha ao cadastrar pedido. Código de status:', response.status_code)
else:
    print("Falha no login:", response.status_code)
