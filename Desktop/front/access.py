import requests #pip install requests
from tkinter import messagebox #pip install tkinter

#api para obter o token de acesso
api_login = "http://localhost:8080/skygreen/auth/login"
api_cadastrarFornecedor = "http://localhost:8080/skygreen/fornecedor/adicionar"
api_listarFornecedores = "http://localhost:8080/skygreen/fornecedor/"

class Access:
    token = None
    @staticmethod #deixa a função como estatica, não precisando passar o self
    def login(user,senha,app):
        login_data = {
            "cpf": f"{user}",
            "senha": f"{senha}"
        }
        try:  
            response = requests.post(api_login, json=login_data)
            
            if response.status_code == 200:
                Access.token = response.json().get("token")
                #print(Access.token)
                app.iniciar_interface()
            else:
                
                app.retornar_login() 
                return True

        except requests.exceptions.RequestException:
                messagebox.showinfo(title="Erro",message=f"Erro de Conexão")
                app.retornar_login()
    
    def cadatroFornecedor(s,e,t,end,cid,est,pais,ie,rs,cnpj,sementeid):
        
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
                print('Fornecedor Adicionado',response.json())
                return True
            else:
                
                print('Fornecedor Não Adicionado',response.status_code)
                return False
                
        except requests.exceptions.RequestException:
                messagebox.showinfo(title="Erro",message=f"Erro de Conexão")
        
    def buscarFornecedores():
        headers = {
            "Authorization": f"Bearer {Access.token}"
        }

        try:
            response = requests.get(api_listarFornecedores, headers=headers)
            
            if response.status_code == 200:
                fornecedores_api = response.json()
                fornecedores = []
                for fornecedor in fornecedores_api:
                    fornecedores.append({
                        "id": f"{fornecedor.get('fornecedorId')}",
                        "nome": fornecedor.get('razaoSocial'),
                        "cnpj": fornecedor.get('cnpj'),
                        "endereço": fornecedor.get('endereco')
                    })
                return fornecedores 
            else:
                print('Falha ao listar fornecedores:', response.status_code)
                print('Resposta:', response.text)

        except requests.exceptions.RequestException:
            messagebox.showinfo(title="Erro", message="Erro de Conexão")   



