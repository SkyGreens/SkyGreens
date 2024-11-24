import customtkinter as ctk  # pip install customtkinter
from access import Access
from style import Style, MessageBox

class cdPedidoCompra:
    
    def __init__(self, callback, dados=None, editar=None):
        self.jn_x = 640
        self.jn_y = 230
        
        self.callback = callback
        self.dados = dados
        self.editar = editar

        titulo = "Cadastrar Pedido" if editar is None else "Consultar Pedido"
        self.root = Style.criar_janela_flutuante(titulo, self.jn_x, self.jn_y)
        self.elementos_tela(self.root)
        self.root.mainloop()
    
    def atualizar_pagina(self, i=0):
        self.root.destroy()
        self.dados = None
        if i == 1:
            from telas.tela_pedidoCompra import pedidoCompra
            pedidoCompra.compras_lista(self.callback)
    
    def voltar_pagina(self, root):
        root.destroy()
    
    def opcaomenu_semente(self, choice, opmenu_var):
        if choice is None:
            opmenu_var.set('Materia Prima')
        self.semente_selecionada_id = choice
        
    def opcaomenu_fornecedor(self, fornecedor_id, opmenu_var_fornecedor):
        
        self.fornecedor_selecionado_id = fornecedor_id

        if fornecedor_id:
            sementes = Access.listarSementesFornecedor(fornecedor_id)
        else:
            sementes = []

        id_sementes = {"" : None}
        nomes_sementes = [""]

        for semente in sementes:
            id_sementes[semente['nome']] = semente['id']
            nomes_sementes.append(semente['nome'])

        self.widgets['sementes'].configure(values=nomes_sementes)
        self.opmenu_var_semente.set("Selecione a Semente")
    
    def cadastrar_pedido(self):
        msg_box = MessageBox()
        
        quantidade = int(self.widgets['quantidade'].get())
        nome_fornecedor = self.widgets['fornecedor'].get()
        fornecedorid = self.id_fornecedores.get(nome_fornecedor)
        sementeid = self.semente_selecionada_id
        
        result = Access.cadastroPedidoCompra(fornecedorid, quantidade, sementeid)
        if result:
            msg_box.showinfo_autoclose("Pedido cadastrado com sucesso!")
            self.atualizar_pagina(1)
        else:
            msg_box.showinfo_autoclose("Pedido não cadastrado!")
        
    def elementos_tela(self, root):
        estado_campo = "normal" if self.editar != 0 else "disabled"
        campos = [('Quantidade', 'quantidade', 1)]
        
        self.widgets = {}
        
        list_fornecedores = Access.listarFornecedores()
        self.id_fornecedores = {"" : None}
        nomes_fornecedores = [""]

        for fornecedor in list_fornecedores:
            self.id_fornecedores[fornecedor['nome']] = fornecedor['id']
            nomes_fornecedores.append(fornecedor['nome'])
        
        self.opmenu_var_fornecedor = ctk.StringVar(value='Selecione o Fornecedor')
        self.widgets['fornecedor'] = ctk.CTkOptionMenu(root, width=620, height=35, values=nomes_fornecedores, variable=self.opmenu_var_fornecedor,
            command=lambda choice: self.opcaomenu_fornecedor(self.id_fornecedores[choice], self.opmenu_var_fornecedor),fg_color=Style.color('fg'))
        self.widgets['fornecedor'].grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.widgets['fornecedor'].configure(state=estado_campo)

        for (placeholder, comp_nome, row, *column) in campos:
            col = column[0] if column else 0

            self.widgets[comp_nome] = ctk.CTkEntry(root, width=620 if not column else 300, height=35, placeholder_text=placeholder)

            if self.dados:
                if comp_nome == 'quantidade' and 'qtd' in self.dados:
                    valor = self.dados['qtd']
                    if valor:
                        self.widgets[comp_nome].insert(0, valor)
            
            self.widgets[comp_nome].configure(state=estado_campo)
            self.widgets[comp_nome].grid(row=row, column=col, columnspan=2 if not column else 1, padx=10, pady=10)

        list_sementes = Access.listarSementes()
        id_sementes = {"" : None}
        nomes_sementes = [""]

        for semente in list_sementes:
            id_sementes[semente['nome']] = semente['id']
            nomes_sementes.append(semente['nome'])

        self.opmenu_var_semente = ctk.StringVar(value='Selecione a Semente')
        self.widgets['sementes'] = ctk.CTkOptionMenu(root, width=620, height=35, values=[""], variable=self.opmenu_var_semente,
            command=lambda choice: self.opcaomenu_semente(id_sementes[choice], self.opmenu_var_semente),fg_color=Style.color('fg'))
        self.widgets['sementes'].grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.widgets['sementes'].configure(state=estado_campo)

        if self.dados and 'semente' in self.dados:
            nome_semente = self.dados['semente']['nome']
            if nome_semente in id_sementes:
                self.opmenu_var_semente.set(nome_semente)
                
        if self.dados and 'fornecedor' in self.dados:
            razao_social = self.dados['fornecedor']['razaoSocial']
            if razao_social in self.id_fornecedores:
                self.opmenu_var_fornecedor.set(razao_social)

        if self.editar != 0:
            btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.voltar_pagina(root),
                                        fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_cancelar.grid(row=6, column=0, padx=10, pady=10)

            btn_salvar = ctk.CTkButton(root, width=300, height=35, text='Salvar Pedido', command=self.cadastrar_pedido,
                                        fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_salvar.grid(row=6, column=1, padx=10, pady=10)
        else:
            btn_ok = ctk.CTkButton(root, width=300, height=35, text='Ok', command=lambda: self.voltar_pagina(root),
                                fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_ok.grid(row=6, column=0, columnspan=2, padx=10, pady=10)