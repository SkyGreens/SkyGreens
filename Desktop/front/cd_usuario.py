import customtkinter as ctk # pip install customtkinter
from tkinter import Toplevel # pip install tkinter
import random

from access import Access

fg = "#316133"  # Cor para botões
hover = "#5d732f"  # Cor ao passar o mouse
bg = "#D9D9D9"  # Cor de fundo

class cdUsuario:
    def __init__(self, callback, dados=None,editar=None):
        jn_x = 640
        jn_y = 300
        
        self.callback = callback
        self.dados = dados
        self.editar = editar
        
        self.root = Toplevel()
        self.root.title("Consultar Fornecedor" if editar == 0 else "Editar Fornecedor" if editar == 1 else "Cadastrar Fornecedor")
        self.root.geometry(f"{jn_x}x{jn_y}")
        self.root.wm_attributes('-toolwindow', 1)
        self.root.configure(background=bg)
        
        self.centralizar_janela(self.root, jn_x, jn_y)
        self.elementos_tela(self.root)
        self.root.maxsize(jn_x, jn_y)
        self.root.minsize(jn_x, jn_y)
        self.root.mainloop()

    def centralizar_janela(self,root, largura, altura):

        tela_largura = root.winfo_screenwidth()
        tela_altura = root.winfo_screenheight()

        x = (tela_largura // 2) - (largura // 2)
        y = (tela_altura // 2) - (altura // 2)

        root.geometry(f"{largura}x{altura}+{x}+{y}")
    
    def atualizar_pagina(self,i=0):
        self.root.destroy()
        self.dados = None
        if i == 1:
            from tela_usuario import telaUsuarios
            telaUsuarios.usuario_lista(self.callback)
    
    def modificacao_usuario(self,cpf,cargo, nome, status,email):
        status = "false" if status == "Inativo" else "true"
                
        senha = nome
        
        if self.editar == 1:
            result = Access.editarUsuario()
            #print(f"Usuário Editado\nCPF: {cpf}\nNome: {nome}\nCargo: {cargo}\nSenha: {senha}\nStatus: {status}\nE-mail: {email}")
        else:
            result = Access.cadastroUsuario(cpf,senha,cargo,nome,status,email)
            #print(f"Usuário Cadastrado\nCPF: {cpf}\nNome: {nome}\nCargo: {cargo}\nSenha: {senha}\nStatus: {status}\nE-mail: {email}")
        
        if result:
            self.atualizar_pagina(1)

    def voltar_pagina(self, root):
        root.destroy()

    def switch(self, switch_var):
        switch_var.set("Inativo")

    def elementos_tela(self, root):
        estado_campo = "normal" if self.editar != 0 else "disabled"

        campos = [('CPF', 'cpf', 0), ('Nome', 'nome', 1), ('Email', 'email', 2)]
        self.widgets = {}

        for (placeholder, comp_nome, row, *column) in campos:
            col = column[0] if column else 0

            self.widgets[comp_nome] = ctk.CTkEntry(root, width=620 if not column else 300, height=35, placeholder_text=placeholder)
            
            if self.dados and comp_nome in self.dados:
                valor = self.dados[comp_nome]
                if valor:
                    self.widgets[comp_nome].insert(0, valor)

            self.widgets[comp_nome].configure(state=estado_campo)
            self.widgets[comp_nome].grid(row=row, column=col, columnspan=2 if not column else 1, padx=10, pady=10)

        cargo_map = {"ADMIN": "Administrador","GERENTEPRODUCAO": "Gerente de Produção","ASSISTENTEPRODUCAO": "Assistente de Produção"}

        list_cargos = list(cargo_map.values())
        if self.dados is None:
            cargo_inicial = "ADMIN"
        else:
            cargo_inicial = self.dados.get('cargo', 'ADMIN')  # Valor interno para edição/consulta

        # Converte o valor interno para o valor visual
        cargo_inicial_visual = cargo_map.get(cargo_inicial, "Administrador")
        opmenu_var = ctk.StringVar(value=cargo_inicial_visual)

        self.widgets['cargo'] = ctk.CTkOptionMenu(root, width=300, height=35, values=list_cargos, variable=opmenu_var, fg_color=fg)
        self.widgets['cargo'].grid(row=4, column=0, padx=10, pady=10)
        self.widgets['cargo'].configure(state=estado_campo)
        
        status_inicial = "Ativo" if not self.dados or self.dados.get('status', True) else "Inativo"
        self.switch_var = ctk.StringVar(value=status_inicial)
        self.widgets['status'] = ctk.CTkSwitch(root, textvariable=self.switch_var, width=300, height=35, variable=self.switch_var, onvalue="Ativo", offvalue="Inativo", fg_color=fg)
        self.widgets['status'].grid(row=4, column=1, padx=10, pady=10)
        self.widgets['status'].configure(state=estado_campo)

        if self.editar != 0:
            btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.voltar_pagina(root),fg_color=fg,hover_color=hover)
            btn_cancelar.grid(row=5, column=0, padx=10, pady=10)
            
            btn_texto = 'Atualizar' if self.dados else 'Registrar'
            btn_registrar = ctk.CTkButton(root, width=300, height=35, text=btn_texto, command=lambda: self.modificacao_usuario(
                self.widgets['cpf'].get(),cargo_inicial, self.widgets['nome'].get(), self.widgets['status'].get(),self.widgets['email'].get()),fg_color=fg,hover_color=hover)
            btn_registrar.grid(row=5, column=1, padx=10, pady=10)
        else:
            btn_ok = ctk.CTkButton(root, width=300, height=35, text='Ok', command=lambda: self.voltar_pagina(root),fg_color=fg,hover_color=hover)
            btn_ok.grid(row=5, column=0,columnspan = 2, padx=10, pady=10)
