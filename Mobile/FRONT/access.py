# access.py
import flet as ft
import requests
from datetime import datetime, timezone
from dateutil import parser

API_BASE = "http://localhost:8080/skygreen"

api_url = "http://localhost:8080/skygreen/auth/login"
api_listarPedidosVenda = f"{API_BASE}/vendas/"
api_listarPrateleira = f"{API_BASE}/prateleira/"
api_listarSementes = f"{API_BASE}/sementes/"

class Funcoes:

    def calcular_dias_restantes(data_inicio, tempo_cultivo):
        data_inicio = parser.isoparse(data_inicio)  # Lida com o formato ISO 8601
        data_atual = datetime.now(timezone.utc)
        dias_passados = (data_atual - data_inicio).days  # Calcula a diferença em dias
        dias_restantes = tempo_cultivo - dias_passados  # Subtrai dos dias totais de cultivo

        return dias_restantes if dias_restantes > 0 else 0

class Access:
    token = None
    userId = None
    
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
            
            if response.status_code == 200:
                data = response.json()
                Access.token = data.get("token")
                Access.userId = data.get("userId")

                
                return Access.token, Access.userId, "Login realizado com sucesso", ft.colors.GREEN
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
    
    def listarSementes():
        headers = {"Authorization": f"Bearer {Access.token}"}

        response = requests.get(api_listarSementes, headers=headers)
        
        if response.status_code == 200:
            sementes_api = response.json()
            sementes = []
            for i in sementes_api:
                sementes.append({
                    "id": i.get('sementeId'),
                    "nome": i.get('nome'),
                    "descricao": i.get('descricao')
                })
            return sementes 
        else:
            print('Falha ao listar sementes:',  response.text)
    
        
    def listarPrateleira():
        headers = {"Authorization": f"Bearer {Access.token}"}
        response = requests.get(api_listarPrateleira, headers=headers)
        
        if response.status_code == 200:

            prateleira_api = response.json()
            list_sementes = {semente['id']: semente['nome'] for semente in Access.listarSementes()}
            prateleira = []
            
            for prat in prateleira_api:
                producao = prat.get('producao')
                statusprat = prat.get('disponivel')
                
                if producao and 'dataInicio' in producao and 'tempoCultivo' in producao:
                    diasRestantes = Funcoes.calcular_dias_restantes(producao['dataInicio'], producao['tempoCultivo'])
                    tempoCultivo = producao.get('tempoCultivo')
                else:
                    diasRestantes = None
                    tempoCultivo = None
                
                prateleira.append({
                    "id": prat.get('prateleira_id'),
                    "disponivel": "Produção" if not statusprat else "Disponivel",
                    "producao": {
                        "idseed": producao.get('sementeId'),
                        "nome_semente": list_sementes.get(producao.get('sementeId')),
                        "dataInicio": producao.get('dataInicio'),
                        "status": "Ativo" if producao.get('ativo') else "Inativo",
                        "graf_valor": [tempoCultivo,diasRestantes]
                    } if not statusprat and producao else None
                })

            return prateleira
        else:
            return False