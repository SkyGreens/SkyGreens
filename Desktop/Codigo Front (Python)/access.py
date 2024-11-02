import requests
from tkinter import messagebox

API_BASE = "http://localhost:8080/skygreen"

api_login = f"{API_BASE}/auth/login"

api_cadastrarFornecedor = f"{API_BASE}/fornecedor/adicionar"
api_listarFornecedores = f"{API_BASE}/fornecedor/"
api_editarFornecedores = f"{API_BASE}/fornecedor/update"

api_cadastrarSementes = f"{API_BASE}/sementes/adicionar"
api_listarSementes = f"{API_BASE}/sementes/"

api_perfilUser = f"{API_BASE}/usuario/personal/"
api_listarUsuario = f"{API_BASE}/usuario/"
api_especificoUsuario = f"{API_BASE}/usuario/"
api_cadastrarUsuario = f"{API_BASE}/auth/register"
api_editarUsuario = f"{API_BASE}/usuario/update"

api_cadastrarProducao = f"{API_BASE}/producao/adicionar"
api_listarProducao = f"{API_BASE}/producao/"

class Access:
    token = None
    userId = None
    
    @staticmethod #deixa a função como estatica, não precisando passar o self
    def login(user, senha, app):
        login_data = {
            "cpf": user,
            "senha": senha
        }
        
        try:
            response = requests.post(api_login, json=login_data)
            
            if response.status_code == 200:
                data = response.json()
                Access.token = data.get("token")
                Access.userId = data.get("userId")
                app.iniciar_interface()
            else:
                app.retornar_login()
                return True

        except requests.exceptions.RequestException:
            messagebox.showinfo(title="Erro", message="Erro de Conexão")
            app.retornar_login()

    def cadastroFornecedor(status, email, tel, end, cid, est, pais, ie, rs, cnpj, sementeid=None):
        cadatro_data = {
            "ativo": status,
            "email": email,
            "telefone": tel,
            "endereco": end,
            "cidade": cid,
            "estado": est,
            "pais": pais,
            "inscricaoEstadual": ie,
            "razaoSocial": rs,
            "cnpj": cnpj
        }
        
        if sementeid is not None:
            cadatro_data["sementes"] = [{"sementeId": sementeid}]

        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}

        response = requests.post(api_cadastrarFornecedor, json=cadatro_data, headers=headers)
        
        if response.status_code == 200:
            print('Fornecedor Adicionado')
            return True
        else:
            print('Fornecedor Não Adicionado', response.text)
            return False

    def listarFornecedores():
        headers = {"Authorization": f"Bearer {Access.token}"}

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
            print('Falha ao listar fornecedores:', response.text)

    def editarFornecedor(idfornecedor,status,email,tel,end,cid,est,pais,isced,rzsocial,cnpj,sementeid=None):
        
        data = {
            "fornecedorId" : idfornecedor,
            "ativo" : status,
            "email" : email,
            "telefone" : tel,
            "endereco" : end,
            "cidade" : cid,
            "estado" : est,
            "pais" : pais,
            "inscricaoEstadual" : isced,
            "razaoSocial" : rzsocial,
            "cnpj" : cnpj
        }
        if sementeid is not None:
            data["sementes"] = [{"sementeId": sementeid}]
        
        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}
         
        response = requests.put(api_editarFornecedores, json=data, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def cadastrarSementes(nome,desc):

        data = {
            "nome": nome,
            "descricao": desc
        }

        headers = {"Authorization": f"Bearer {Access.token}"}

        response_semente = requests.post(api_cadastrarSementes, json=data, headers=headers)

        if response_semente.status_code == 200:
            print('Semente cadastrada com sucesso!')
            return True
        else:
            print('Falha ao cadastrar a semente:', response_semente.status_code)
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
    
    def visualizarPerfil():
        
        headers = {"Authorization": f"Bearer {Access.token}"}
            
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
            print('Falha ao acessar informações:',response.text)
            
    def listarUsuarios(comand=None,iduser=None):
        
        headers = {"Authorization": f"Bearer {Access.token}"}

        if comand == 0:
            api_Usuario = f"{api_especificoUsuario}{iduser}"
        else:
            api_Usuario = api_listarUsuario
            
        response = requests.get(api_Usuario, headers=headers)
        
        if response.status_code == 200:
            
            usuarios_api = response.json()
            usuarios = []
            
            for user in usuarios_api:
                
                usuarios.append({
                    "id":user.get('id'),
                    "cpf": user.get('cpf'),
                    "cargo": user.get('role'),
                    "nome": user.get('nome'),
                    "status": user.get('ativo'),
                    "email": user.get('email')
                })
            return usuarios 
        else:
            return False
            print('Falha ao listar fornecedores:', response.text)
  
    def cadastroUsuario(cpf,senha,cargo,nome,status,email):
        
        cadatro_data = {
            "cpf" : f"{cpf}",
            "senha" : f"{senha}",
            "role" : f"{cargo}",
            "nome" : f"{nome}",
            "ativo" : f"{status}",
            "email" : f"{email}"
        }

        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}
        
        response = requests.post(api_cadastrarUsuario, json=cadatro_data, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
                
    def editarUsuario(iduser,cargo,nome,status,email):
        data = {
            "id":iduser,
            "role" : f"{cargo}",
            "nome" : f"{nome}",
            "ativo" : f"{status}",
            "email" : f"{email}"
        }
        
        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}
         
        response = requests.put(api_editarUsuario, json=data, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
                           
    def listarProducao():
        
        headers = {"Authorization": f"Bearer {Access.token}"}

        response = requests.get(api_listarProducao, headers=headers)
        
        if response.status_code == 200:
            producao_api = response.json()
            producao = []
            print(producao_api)
        else:
            print('Falha ao listar Producao:',  response.text)
            
    def cadastrarProducao():
        data = {
            "sementeId":"1",
            "sementeQuantidade": "5",
            "tempoCultivo" : "1",
            "dataInicio" : "2024-05-05",
            "fotoSemente" : "",
            "ativo": "true",
            "prateleiraId" : "2"
        }

        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {Access.token}"}

        response_semente = requests.post(api_cadastrarProducao, json=data, headers=headers)

        if response_semente.status_code == 200:
            print('Producao cadastrada com sucesso!')
            return True
        else:
            print('Falha ao cadastrar a producao:', response_semente.status_code)
            return False
        
    def verificar_permissoes(self,n):
        
        #0 - botao
        perfil = Access.visualizarPerfil()
    
        for i in perfil:
            cargo = i['cargo']

        if cargo == 'GERENTEPRODUCAO' :
            if n == 6:
                return False
            else:
                return True
        elif cargo == 'ASSISTENTEPRODUCAO':
            if n == 6:
                return False
            elif n == 0: #botoes
                return False
            else:
                return True
        else:
            return True