import requests

url_login = "http://localhost:8080/skygreen/auth/login"

login_data = {
    "cpf": "12345678909",
    "senha": "admin"
}

response = requests.post(url_login, json=login_data)

if response.status_code == 200:

    token = response.json().get("token")
    #print(f"Token JWT recebido: {token}")


    url_adicionar_producao = "http://localhost:8080/skygreen/producao/adicionar"


    producoes = [
        {
            "sementeQuantidade": "5",
            "tempoCultivo": "30",
            "dataInicio": "2024-05-22",
            "fotoSemente": "",
            "ativo": "true"
        },
        {
            "sementeQuantidade": "10",
            "tempoCultivo": "45",
            "dataInicio": "2024-06-01",
            "fotoSemente": "",
            "ativo": "true"
        },
        {
            "sementeQuantidade": "8",
            "tempoCultivo": "60",
            "dataInicio": "2024-07-10",
            "fotoSemente": "",
            "ativo": "true"
        },

    ]


    headers = {
        "Authorization": f"Bearer {token}"
    }


    def adicionar_producao(dados_producao):
        response_producao = requests.post(url_adicionar_producao, json=dados_producao, headers=headers)
        if response_producao.status_code == 200:
            print('Produção cadastrada com sucesso:', dados_producao)
        else:
            print('Falha ao cadastrar a produção:', response_producao.status_code)
            print('Resposta:', response_producao.text)

    for producao in producoes:
        adicionar_producao(producao)

else:
    print("Falha no login:", response.status_code)
