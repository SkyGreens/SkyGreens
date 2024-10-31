import customtkinter as ctk  # pip install customtkinter

from style import Style
from access import Access

class cdPedido:
    def __init__(self):
        self.jn_x = 640
        self.jn_y = 400
        
        titulo = ("Cadastrar Pedido")
        self.root = Style.criar_janela_flutuante(titulo, self.jn_x, self.jn_y)
        self.elementos_tela(self.root)
        self.root.mainloop()
        
    def voltar_pagina(self, root):
        root.destroy()
    
    def opcaomenu(self, choice, opmenu_var):
        if choice is None:
            opmenu_var.set('Materia Prima')
        self.semente_selecionada_id = choice
    
    def salvar_pedido(self):
        print(f"Pedido cadastrado: {self.nome_entry.get()}, {self.quantidade_entry.get()} unidades, R$ {self.preco_entry.get()}")
    
    def elementos_tela(self,root):  
        self.semente_selecionada_id = None
        list_sementes = Access.listarSementes()
        id_sementes = {"": None}
        nomes_sementes = [""]
        
        for i in list_sementes:
            id_sementes[i['nome']] = i['id']
            nomes_sementes.append(i['nome'])
        
        opmenu_var = ctk.StringVar(value='Materia Prima')
        self.sementes = ctk.CTkOptionMenu(root, width=620, height=35, values=nomes_sementes, variable=opmenu_var,
                                                command=lambda choice: self.opcaomenu(id_sementes[choice], opmenu_var),fg_color=Style.color('fg'))
        self.sementes.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        en_id = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Id Pedido')
        en_id.grid(row=2,column=0,columnspan=2, padx=10, pady=10)
        
        en_cliente = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Cliente')
        en_cliente.grid(row=3,column=0,columnspan=2, padx=10, pady=10)

        en_qtd= ctk.CTkEntry(root, width=620, height=35, placeholder_text='Quantidade')
        en_qtd.grid(row=4,column=0,columnspan=2, padx=10, pady=10)
        
        en_prazoEntrega = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Prazo da Entrega')
        en_prazoEntrega.grid(row=5,column=0,columnspan=2, padx=10, pady=10)
        
        en_status = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Status')
        en_status.grid(row=6,column=0,columnspan=2, padx=10, pady=10)

        btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.voltar_pagina(root),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
        btn_cancelar.grid(row=7, column=0, padx=10, pady=10)
        
        btn_salvar = ctk.CTkButton(root, width=300, height=35, text='Salvar Pedido', command= self.salvar_pedido,fg_color=Style.color('fg'),hover_color=Style.color('hover'))
        btn_salvar.grid(row=7, column=1, padx=10, pady=10)