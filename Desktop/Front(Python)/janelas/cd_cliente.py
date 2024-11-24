import customtkinter as ctk  # pip install customtkinter
from access import Access

from style import Style,MessageBox

class cdCliente:
    
    def __init__(self,callback, dados=None,editar=None):
        
        self.msg_box = MessageBox()
        self.jn_x = 640
        self.jn_y = 450
        
        self.callback = callback
        self.dados = dados
        self.editar = editar
        
        titulo = ("Consultar Cliente" if editar == 0 else "Editar Cliente" if editar == 1 else "Cadastrar Cliente")
        self.root = Style.criar_janela_flutuante(titulo, self.jn_x, self.jn_y)
        self.elementos_tela(self.root)
        self.root.mainloop()
    
    def atualizar_pagina(self,i=0):
        self.root.destroy()
        self.dados = None
        if i == 1:
            from telas.tela_clientes import telaCliente
            telaCliente.clientes_lista(self.callback)
            
    def voltar_pagina(self, root):
        root.destroy()
        
    def modificacao_cliente(self, cnpj, rzsocial, email, status, tel, end, cid, est, pais):
        status = False if status == "Inativo" else True
        
        if self.editar == 1:
            iduser = self.dados['id']
            result = Access.editarCliente(iduser,status, email, tel, end, cid, est, pais, rzsocial, cnpj)
            if result:
                self.msg_box.showinfo_autoclose(f"Cliente atualizado com sucesso!")
            else:
                self.msg_box.showinfo_autoclose(f"Cliente não atualizado!")
        else:
            result = Access.cadastroCliente(status, email, tel, end, cid, est, pais, rzsocial, cnpj)
            if result:
                self.msg_box.showinfo_autoclose(f"Cliente cadastrado com sucesso!")
            else:
                self.msg_box.showinfo_autoclose(f"Cliente não cadastrado!")
        
        if result:
            self.atualizar_pagina(1)
            
    def switch(self, switch_var):
        switch_var.set("Inativo")
    
    def elementos_tela(self, root):
        campos = [('CNPJ/CPF', 'cnpj', 0), ('Razão Social', 'razaoSocial', 1), ('E-mail', 'email', 2),
            ('Endereço', 'endereco', 3), ('Cidade', 'cidade', 4), 
            ('Telefone', 'telefone', 5, 0), ('Estado', 'estado', 5, 1), ('País', 'pais', 6, 0)]
        
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
        self.widgets['status'].grid(row=6, column=1, padx=10, pady=10)
        self.widgets['status'].configure(state=estado_campo)
        
        if self.editar != 0 :
        
            btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.atualizar_pagina(),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
            btn_cancelar.grid(row=7, column=0, padx=10, pady=10)

            btn_texto = 'Atualizar' if self.dados else 'Registrar'
            btn_registrar = ctk.CTkButton(root, width=300, height=35, text=btn_texto, command=lambda: self.modificacao_cliente(
                self.widgets['cnpj'].get(), self.widgets['razaoSocial'].get(), self.widgets['email'].get(),
                self.widgets['status'].get(), self.widgets['telefone'].get(), self.widgets['endereco'].get(), self.widgets['cidade'].get(), 
                self.widgets['estado'].get(), self.widgets['pais'].get()),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
            btn_registrar.grid(row=7, column=1, padx=10, pady=10)
        else:
            btn_ok = ctk.CTkButton(root, width=300, height=35, text='Ok', command=lambda: self.voltar_pagina(root),
                                   fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_ok.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
