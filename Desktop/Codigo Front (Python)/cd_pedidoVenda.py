import customtkinter as ctk  # pip install customtkinter
from access import Access
from style import Style, MessageBox

class cdPedidoVenda:
    
    def __init__(self, callback, dados=None, editar=None):
        self.jn_x = 640
        self.jn_y = 290
        
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
            from tela_pedidoVenda import pedidoVenda
            pedidoVenda.vendas_lista(self.callback)
    
    def voltar_pagina(self, root):
        root.destroy()
    
    def opcaomenu(self, choice, opmenu_var):
        if choice is None:
            opmenu_var.set('Escolha')
        self.semente_selecionada_id = choice
    
    def cadastrar_pedido(self):
        msg_box = MessageBox()
        
        quantidade = int(self.widgets['qtd'].get())
        tempoCultivo = int(self.widgets['tempocultivo'].get())
        clienteid = self.id_clientes.get(self.widgets['cliente'].get())
        sementeid = self.semente_selecionada_id
        
        result = Access.cadastroPedidoVenda(clienteid, quantidade, sementeid,tempoCultivo)
        
        
        if result:
            msg_box.showinfo_autoclose("Pedido cadastrado com sucesso!")
            self.atualizar_pagina(1)
        else:
            msg_box.showinfo_autoclose("Pedido não cadastrado!")
        
    def elementos_tela(self, root):
        estado_campo = "normal" if self.editar != 0 else "disabled"
        campos = [('Quantidade', 'qtd', 2),('Tempo de Cultivo', 'tempocultivo', 3)]
        self.widgets = {}
        
        list_cliente = Access.listarClientes()
        self.id_clientes = {"" : None}
        nomes_clientes = [""]

        for cli in list_cliente:
            self.id_clientes[cli['razaoSocial']] = cli['clienteid']
            nomes_clientes.append(cli['razaoSocial'])
        
        opmenu_var_Cliente = ctk.StringVar(value='Selecione o Cliente')
        self.widgets['cliente'] = ctk.CTkOptionMenu(root, width=620, height=35, values=nomes_clientes, variable=opmenu_var_Cliente,
            command=lambda choice: self.opcaomenu(self.id_clientes[choice], opmenu_var_Cliente),fg_color=Style.color('fg'))
        self.widgets['cliente'].grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.widgets['cliente'].configure(state=estado_campo)

        for (placeholder, comp_nome, row, *column) in campos:
            col = column[0] if column else 0

            self.widgets[comp_nome] = ctk.CTkEntry(root, width=620 if not column else 300, height=35, placeholder_text=placeholder)

            if self.dados and comp_nome in self.dados:
                valor = self.dados[comp_nome]
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

        opmenu_var_semente = ctk.StringVar(value='Selecione a Semente')
        self.widgets['sementes'] = ctk.CTkOptionMenu(root, width=620, height=35, values=nomes_sementes, variable=opmenu_var_semente,
            command=lambda choice: self.opcaomenu(id_sementes[choice], opmenu_var_semente),fg_color=Style.color('fg'))
        self.widgets['sementes'].grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.widgets['sementes'].configure(state=estado_campo)

        if self.dados and 'semente' in self.dados:
            nome_semente = self.dados['semente']['nome']
            if nome_semente in id_sementes:
                opmenu_var_semente.set(nome_semente)
                
        if self.dados and 'cliente' in self.dados:
            razao_social = self.dados['cliente']['razaoSocial']
            if razao_social in self.id_clientes:
                opmenu_var_Cliente.set(razao_social)

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