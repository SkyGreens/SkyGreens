# access.py
import flet as ft
import requests

class Access:
    @staticmethod
    def login(cpf, senha):
        api_url = "http://192.168.31.243:8080/skygreen/auth/login"
        payload = {
            "cpf": cpf,
            "senha": senha
        }
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(api_url, json=payload, headers=headers)
            print(f"Status da resposta: {response.status_code}")
            print(f"Conteúdo da resposta: {response.text}")
            
            if response.status_code == 200:
                data = response.json()
                token = data.get("token")
                userId = data.get("userId")
                
                print(f"Token recebido: {token}")
                print(f"ID do usuário: {userId}")
                
                return token, userId, "Login realizado com sucesso", ft.colors.GREEN
            else:
                return None, None, "CPF ou senha inválidos.", ft.colors.RED
        
        except Exception as ex:
            print(f"Erro: {ex}")
            return None, None, f"Erro ao se conectar com a API: {ex}", ft.colors.RED

