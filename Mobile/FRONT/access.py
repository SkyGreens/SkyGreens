# access.py
import flet as ft
import requests

API_BASE = "http://localhost:8080/skygreen"

api_url = "http://localhost:8080/skygreen/auth/login"
api_listarPedidosVenda = f"{API_BASE}/vendas/"

class Access:
    
    def __init__(self, token):
        self.token = token
        self.api_url = "http://localhost:8080/skygreen/auth/login"
    
    @staticmethod
    def login(cpf, senha):
        api_url = "http://localhost:8080/skygreen/auth/login"
        payload = {
            "cpf": cpf,
            "senha": senha
        }
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(api_url, json=payload, headers=headers)
            #print(f"Status da resposta: {response.status_code}")
            #print(f"Conteúdo da resposta: {response.text}")
            
            if response.status_code == 200:
                data = response.json()
                token = data.get("token")
                userId = data.get("userId")
                
                #print(f"Token recebido: {token}")
                #print(f"ID do usuário: {userId}")
                
                return token, userId, "Login realizado com sucesso", ft.colors.GREEN
            else:
                return None, None, "CPF ou senha inválidos.", ft.colors.RED
        
        except Exception as ex:
            print(f"Erro: {ex}")
            return None, None, f"Erro ao se conectar com a API: {ex}", ft.colors.RED
        
    def obter_pedidos(self):
        # Usando a URL correta para acessar o endpoint de pedidos
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{API_BASE}/vendas/", headers=headers)
        
        if response.status_code == 200:
            return response.json()  # Retorna a lista de pedidos
        else:
            response.raise_for_status()  # Levanta erro se status for diferente de 200