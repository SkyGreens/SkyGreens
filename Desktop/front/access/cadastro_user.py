import requests

# URL para a qual a requisição POST será enviada
url = 'http://localhost:8080/skygreen/auth/register'

# Dados a serem enviados no corpo da requisição
data = {
    "cpf" : "08699133871",
    "senha" : "123456789",
    "role" : "GERENTEPRODUCAO",
    "nome" : "PEDRO",
    "ativo" : "true",
    "email" : "teste3@gmail.com"
}

headers = {
    'Content-Type': 'application/json'

}
# Fazer a requisição POST
response = requests.post(url, json=data, headers=headers)

# Verificar a resposta
if response.status_code == 200:
    print('Requisição bem-sucedida!')
    print('Resposta:', response.status_code)
else:
    print('Falha na requisição. Código de status:', response.status_code)