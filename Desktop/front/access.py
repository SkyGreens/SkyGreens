import requests #pip install requests
from tkinter import messagebox #pip install tkinter

#api para obter o token de acesso
api_login = "http://localhost:8080/skygreen/auth/login"
api_cadastrarFornecedor = "http://localhost:8080/skygreen/fornecedor/adicionar"
api_listarFornecedores = "http://localhost:8080/skygreen/fornecedor/"
api_listarSementes = "http://localhost:8080/skygreen/sementes/listar"
api_perfilUser = "http://localhost:8080/skygreen/usuario/personal/"

class Access:
    token = None
    userId = None
    @staticmethod #deixa a função como estatica, não precisando passar o self
    def login(user,senha,app):
        login_data = {
            "cpf": f"{user}",
            "senha": f"{senha}"
        }
        try:  
            response = requests.post(api_login, json=login_data)
            
            if response.status_code == 200:
                Access.token = response.json().get("tokenk")
                Access.userId = response.json().get("userId")
                app.iniciar_interface()
            else:
                app.retornar_login()
                return True

        except requests.exceptions.RequestException:
                messagebox.showinfo(title="Erro",message=f"Erro de Conexão")
                app.retornar_login()
    
    def cadatroFornecedor(s,e,t,end,cid,est,pais,ie,rs,cnpj,sementeid):
        
        if sementeid == None:
            cadatro_data = {
                "ativo": f"{s}",
                "email": f"{e}",
                "telefone": f"{t}",
                "endereco": f"{end}",
                "cidade": f"{cid}",
                "estado": f"{est}",
                "pais": f"{pais}",
                "inscricaoEstadual": f"{ie}",
                "razaoSocial": f"{rs}",
                "cnpj": f"{cnpj}"
            }
        else:
            cadatro_data = {
                "ativo": f"{s}",
                "email": f"{e}",
                "telefone": f"{t}",
                "endereco": f"{end}",
                "cidade": f"{cid}",
                "estado": f"{est}",
                "pais": f"{pais}",
                "inscricaoEstadual": f"{ie}",
                "razaoSocial": f"{rs}",
                "cnpj": f"{cnpj}",
                "sementes":[ {
                    "sementeId":sementeid
                }]
            }
            
        headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {Access.token}"
        }
        
        try:  
            response = requests.post(api_cadastrarFornecedor, json=cadatro_data, headers=headers)
            if response.status_code == 200:
                print('Fornecedor Adicionado')
                return True
            else:
                
                print('Fornecedor Não Adicionado',response.status_code)
                return False
                
        except requests.exceptions.RequestException:
                messagebox.showinfo(title="Erro",message=f"Erro de Conexão")
        
    def listarFornecedores():
        headers = {
            "Authorization": f"Bearer {Access.token}"
        }

        try:
            response = requests.get(api_listarFornecedores, headers=headers)
            
            if response.status_code == 200:
                
                fornecedores_api = response.json()
                fornecedores = []
                
                for fornecedor in fornecedores_api:
                    sementes = fornecedor.get('sementes', [])
                    
                    if sementes:
                        nomesemente = sementes[0].get('nome', '')
                    else:
                        nomesemente = ''
                    
                    fornecedores.append({
                        "id": f"{fornecedor.get('fornecedorId')}",
                        "nome": fornecedor.get('razaoSocial'),
                        "cnpj": fornecedor.get('cnpj'),
                        "endereco": fornecedor.get('endereco'),
                        "status": fornecedor.get('ativo'),
                        "email": fornecedor.get('email'),
                        "telefone": fornecedor.get('telefone'),
                        "cidade": fornecedor.get('cidade'),
                        "estado": fornecedor.get('estado'),
                        "pais": fornecedor.get('pais'),
                        "inscricaoEstadual": fornecedor.get('inscricaoEstadual'),
                        "semente":nomesemente
                    })
                return fornecedores 
            else:
                print('Falha ao listar fornecedores:', response.status_code)
                print('Resposta:', response.text)

        except requests.exceptions.RequestException:
            messagebox.showinfo(title="Erro", message="Erro de Conexão")   

    def listarSementes():
        headers = {
            "Authorization": f"Bearer {Access.token}"
        }

        try:
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
                print('Falha ao listar sementes:', response.status_code)
                print('Resposta:', response.text)

        except requests.exceptions.RequestException:
            messagebox.showinfo(title="Erro", message="Erro de Conexão") 

    def editarFornecedor(id,s,e,t,end,cid,est,pais,ie,rs,cnpj,sementeid):
        print('Fornecedor Atualizado: ',id)
        return True
    
    def visualizarPerfil():
        
        headers = {
            "Authorization": f"Bearer {Access.token}"
        }

        try:
            api_MperfilUser = f"{api_perfilUser}{Access.userId}"
            response = requests.get(api_MperfilUser, headers=headers)
            
            if response.status_code == 200:
                perfil_api = response.json()
                dados_perfil = []
                
                dados_perfil.append({
                    "id": perfil_api.get('id'),
                    "email": perfil_api.get('email'),
                    "ativo": perfil_api.get('ativo'),
                    "cargo": perfil_api.get('role'),
                    "nome": perfil_api.get('nome'),
                    "cpf": perfil_api.get('cpf') 
                })
                return dados_perfil
            
            else:
                print('Falha ao acessar informações:', response.status_code)
                print('Resposta:', response.text)

        except requests.exceptions.RequestException:
            messagebox.showinfo(title="Erro", message="Erro de Conexão")