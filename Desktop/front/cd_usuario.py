import customtkinter as ctk  # pip install customtkinter

from style import Style,MessageBox
from access import Access

class cdUsuario:
    
    def __init__(self, callback, dados=None, editar=None):
        
        self.jn_x = 640
        self.jn_y = 290
        self.callback = callback
        self.dados = dados
        self.editar = editar

        titulo = ("Consultar Fornecedor" if editar == 0 else "Editar Fornecedor" if editar == 1 else "Cadastrar Fornecedor")

        self.root = Style.criar_janela_flutuante(titulo, self.jn_x, self.jn_y)
        
        self.elementos_tela(self.root)
        self.root.mainloop()
        
    def atualizar_pagina(self, i=0):
        self.root.destroy()
        self.dados = None
        if i == 1:
            from tela_usuario import telaUsuarios
            telaUsuarios.usuario_lista(self.callback)

    def modificacao_usuario(self, cpf, cargo, nome, status, email):
        
        msg_box = MessageBox()
        status = "false" if status == "Inativo" else "true"

        senha = cpf[0:3]
        
        if self.editar == 1:
            iduser = self.dados['id']
            result = Access.editarUsuario(iduser, cargo, nome, status, email)
            if result:
                msg_box.showinfo_autoclose(f"Usuario atualizado com sucesso!")
            else:
                msg_box.showinfo_autoclose(f"Usuario não atualizado!")
                
        else:
            result = Access.cadastroUsuario(cpf, senha, cargo, nome, status, email)
            if result:
                msg_box.showinfo_autoclose(f"Usuario cadastrado com sucesso!")
            else:
                msg_box.showinfo_autoclose(f"Usuario não cadastrado!")

        if result:
            self.atualizar_pagina(1)
        
    def voltar_pagina(self, root):
        root.destroy()
        
    def opcaomenu(self, choice, opmenu_var):
        if choice is None:
            opmenu_var.set('Administrador')
        
        if choice == 1:
            escolha = "ADMIN"
        elif choice == 2:
            escolha = "GERENTEPRODUCAO"
        elif choice == 3:
            escolha = "ASSISTENTEPRODUCAO"
            
        self.cargo_selecionado_interno = escolha

    def switch(self, switch_var):
        switch_var.set("Inativo")

    def elementos_tela(self, root):
        estado_campo = "normal" if self.editar != 0 else "disabled"

        campos = [('CPF', 'cpf', 0), ('Nome', 'nome', 1),('Email', 'email', 2)]
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
            
        if self.editar == 1:
            self.widgets['cpf'].configure(state="disabled")
            
        cargo_map = {"ADMIN": "Administrador", "GERENTEPRODUCAO": "Gerente de Produção","ASSISTENTEPRODUCAO": "Assistente de Produção"}
        cargo_map_invertido = {"Administrador": 1, "Gerente de Produção":2, "Assistente de Produção": 3}

        self.cargo_selecionado_interno = None
        list_cargos = list(cargo_map.values())

        opmenu_var = ctk.StringVar(value=cargo_map.get((self.dados.get('cargo'))) if self.dados and cargo_map.get((self.dados.get('cargo'))) else 'Escolha o Cargo')
        self.widgets['cargo'] = ctk.CTkOptionMenu(root, width=300, height=35, values=list_cargos, variable=opmenu_var, fg_color=Style.color('fg')
                                                  ,command=lambda choice: self.opcaomenu(cargo_map_invertido[choice],opmenu_var))
        self.widgets['cargo'].grid(row=4, column=0, padx=10, pady=10)
        self.widgets['cargo'].configure(state=estado_campo)
            
        status_inicial = "Ativo" if not self.dados or self.dados.get(
            'status', True) else "Inativo"
        self.switch_var = ctk.StringVar(value=status_inicial)
        self.widgets['status'] = ctk.CTkSwitch(root, textvariable=self.switch_var, width=300,
                                               height=35, variable=self.switch_var, onvalue="Ativo", offvalue="Inativo", fg_color=Style.color('fg'))
        self.widgets['status'].grid(row=4, column=1, padx=10, pady=10)
        self.widgets['status'].configure(state=estado_campo)

        
        if self.editar != 0:
            btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar',
                                         command=lambda: self.voltar_pagina(root), fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_cancelar.grid(row=6, column=0, padx=10, pady=10)

            btn_texto = 'Atualizar' if self.dados else 'Registrar'
            btn_registrar = ctk.CTkButton(root, width=300, height=35, text=btn_texto, command=lambda: self.modificacao_usuario(
                self.widgets['cpf'].get(), self.cargo_selecionado_interno, self.widgets['nome'].get(), self.widgets['status'].get(), self.widgets['email'].get()), fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_registrar.grid(row=6, column=1, padx=10, pady=10)
        else:
            btn_ok = ctk.CTkButton(root, width=300, height=35, text='Ok', command=lambda: self.voltar_pagina(
                root), fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_ok.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
