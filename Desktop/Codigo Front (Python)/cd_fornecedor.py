import customtkinter as ctk  # pip install customtkinter
from access import Access

from style import Style,MessageBox

class cdFornecedor:
    
    def __init__(self,callback, dados=None,editar=None):
            
        self.jn_x = 640
        self.jn_y = 560
        
        self.callback = callback
        self.dados = dados
        self.editar = editar
        
        titulo = ("Consultar Fornecedor" if editar == 0 else "Editar Fornecedor" if editar == 1 else "Cadastrar Fornecedor")
        self.root = Style.criar_janela_flutuante(titulo, self.jn_x, self.jn_y)
        self.elementos_tela(self.root)
        self.root.mainloop()
    
    def atualizar_pagina(self,i=0):
        self.root.destroy()
        self.dados = None
        if i == 1:
            from tela_fornecedor import telaFornecedor
            telaFornecedor.fornecedor_lista(self.callback)
            
    def voltar_pagina(self, root):
        root.destroy()
        
    def modificacao_fornecedor(self, cnpj, rzsocial, isced, email, status, tel, end, cid, est, pais, semente):
        msg_box = MessageBox()
        status = False if status == "Inativo" else True
        
        if self.editar == 1:
            iduser = self.dados['id']
            result = Access.editarFornecedor(iduser, status, email, tel, end, cid, est, pais, isced, rzsocial, cnpj, semente)
            if result:
                msg_box.showinfo_autoclose(f"Fornecedor atualizado com sucesso!")
            else:
                msg_box.showinfo_autoclose(f"Fornecedor não atualizado!")
        else:
            result = Access.cadastroFornecedor(status, email, tel, end, cid, est, pais, isced, rzsocial, cnpj, semente)
            if result:
                msg_box.showinfo_autoclose(f"Fornecedor cadastrado com sucesso!")
            else:
                msg_box.showinfo_autoclose(f"Fornecedor não cadastrado!")
        
        if result:
            self.atualizar_pagina(1)
            
    def switch(self, switch_var):
        switch_var.set("Inativo")
    
    def opcaomenu(self, choice, opmenu_var):
        if choice is None:
            opmenu_var.set('Semente')
        self.semente_selecionada_id = choice
    
    def elementos_tela(self, root):
        campos = [
            ('CNPJ', 'cnpj', 0), ('Razão Social', 'nome', 1), ('Inscrição Estadual', 'inscricaoEstadual', 2), 
            ('E-mail', 'email', 3), ('Endereço', 'endereco', 4), ('Cidade', 'cidade', 5), 
            ('Telefone', 'telefone', 6, 0), ('Estado', 'estado', 6, 1), ('País', 'pais', 7, 0)
        ]
        estado_campo = "normal" if self.editar != 0 else "disabled"
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

        self.switch_var = ctk.StringVar(value="Ativo" if not self.dados or self.dados.get('status', True) else "Inativo")
        self.widgets['status'] = ctk.CTkSwitch(root, textvariable=self.switch_var, width=300, height=35, variable=self.switch_var, onvalue="Ativo", offvalue="Inativo",fg_color=Style.color('fg'))
        self.widgets['status'].grid(row=7, column=1, padx=10, pady=10)
        self.widgets['status'].configure(state=estado_campo)

        self.semente_selecionada_id = None
        list_sementes = Access.listarSementes()
        id_sementes = {"": None}
        nomes_sementes = [""]
        
        for i in list_sementes:
            id_sementes[i['nome']] = i['id']
            nomes_sementes.append(i['nome'])
        
        opmenu_var = ctk.StringVar(value=self.dados.get('semente') if self.dados and self.dados.get('semente') else 'Materia Prima')
        self.widgets['sementes'] = ctk.CTkOptionMenu(root, width=620, height=35, values=nomes_sementes, variable=opmenu_var,
                                                command=lambda choice: self.opcaomenu(id_sementes[choice], opmenu_var),fg_color=Style.color('fg'))
        self.widgets['sementes'].grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        self.widgets['sementes'].configure(state=estado_campo)
        
        if self.editar != 0 :
        
            btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.atualizar_pagina(),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
            btn_cancelar.grid(row=9, column=0, padx=10, pady=10)

            btn_texto = 'Atualizar' if self.dados else 'Registrar'
            btn_registrar = ctk.CTkButton(root, width=300, height=35, text=btn_texto, command=lambda: self.modificacao_fornecedor(
                self.widgets['cnpj'].get(), self.widgets['nome'].get(), self.widgets['inscricaoEstadual'].get(), self.widgets['email'].get(),
                self.widgets['status'].get(), self.widgets['telefone'].get(), self.widgets['endereco'].get(), self.widgets['cidade'].get(), 
                self.widgets['estado'].get(), self.widgets['pais'].get(), self.semente_selecionada_id
            ),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
            btn_registrar.grid(row=9, column=1, padx=10, pady=10)
        else:
            btn_ok = ctk.CTkButton(root, width=300, height=35, text='Ok', command=lambda: self.voltar_pagina(root),
                                   fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_ok.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
