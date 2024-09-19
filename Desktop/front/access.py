import requests #pip install requests

#api para obter o token de acesso
api_login = "http://localhost:8080/skygreen/auth/login"

class Access:
    @staticmethod #deixa a função como estatica, não precisando passar o self
    def login(user,senha):
        login_data = {
            "cpf": f"{user}",
            "senha": f"{senha}"
        }

        response = requests.post(api_login, json=login_data)
        
        if response.status_code == 200:
            
            global token
            token = response.json().get("token")
            print("Entrou")

        else:
            print("Erro ao entrar")


