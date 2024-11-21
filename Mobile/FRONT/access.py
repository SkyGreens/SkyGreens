import flet as ft
import requests
from datetime import datetime, timezone
from dateutil import parser

API_BASE = "http://localhost:8080/skygreen"

api_login = f"{API_BASE}/auth/login"

api_listarPedidosVenda = f"{API_BASE}/vendas/"
api_listarPrateleira = f"{API_BASE}/prateleira/"
api_listarSementes = f"{API_BASE}/sementes/"
api_listarEstoque = f"{API_BASE}/estoque/"
api_listarPedidosVenda = f"{API_BASE}/vendas/"
api_listarProducao = f"{API_BASE}/producao/"

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
    
    @staticmethod
    def login(cpf, senha):

        payload = {"cpf": cpf,"senha": senha}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(api_login, json=payload, headers=headers)
            
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
        
    def listarpedidosVenda():
        headers = {"Authorization": f"Bearer {Access.token}"}
            
        response = requests.get(api_listarPedidosVenda, headers=headers)
        
        if response.status_code == 200:
            
            vendas_api = response.json()
            listvendas = []
    
            for vendas in vendas_api:
                
                listvendas.append({
                    "idvenda":vendas.get('pedidoVendaId'),
                    "cliente":vendas.get('cliente'),
                    "qtd":vendas.get('quantidade'),
                    "semente":vendas.get('semente'),
                    "tempocultivo":vendas.get('tempoCultivo'),
                    "status":vendas.get('ativo')
                })
            return listvendas 
        else:
            return False
    
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
                        "tempoCultivo": tempoCultivo,
                        "tempoRestante":diasRestantes
                    } if not statusprat and producao else None
                })

            return prateleira
        else:
            return False
        
    def listarEstoque():
        headers = {"Authorization": f"Bearer {Access.token}"}

        response = requests.get(api_listarEstoque, headers=headers)
        
        if response.status_code == 200:
            estoque_api = response.json()
            estoque = []
        
            for est in estoque_api:
                semente = est.get('semente')
                
                estoque.append({
                    "id": f"{est.get('estoqueId')}",
                    "qtd": est.get('quantidade'),
                    "nome_semente": semente.get('nome'),
                    "desc": semente.get('descricao')
                })
            return estoque
        else:
            print('Falha ao listar Estoque:', response.text)
            
    def listarProducao():
        
        headers = {"Authorization": f"Bearer {Access.token}"}

        response = requests.get(api_listarProducao, headers=headers)
        
        if response.status_code == 200:
            producao_api = response.json()
            producao = []
            list_sementes = Access.listarSementes()
            
            def nome_semente(id_semente):
                for semente in list_sementes:
                    if semente['id'] == id_semente:
                        return semente['nome']
                return None
            
            for prod in producao_api:
                id_semente = prod.get('sementeId')
                producao.append({
                    "id": prod.get('producaoId'),
                    "nome_semente": nome_semente(id_semente),
                    "qtd": prod.get('sementeQuantidade'),
                    "status": "Ativo" if prod.get('ativo') == True else "Inativo",
                    "tempoCultivo": prod.get('tempoCultivo'),
                    "diasRestantes": Funcoes.calcular_dias_restantes(prod.get('dataInicio'), prod.get('tempoCultivo')),
                    "dataInicio": prod.get('dataInicio')
                })
            return producao
        else:
            print('Falha ao listar Producao:', response.text)