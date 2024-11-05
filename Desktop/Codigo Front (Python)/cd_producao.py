import customtkinter as ctk # pip install customtkinter

from access import Access
from style import Style,MessageBox

class cdProducao:
    
    def __init__(self,callback):
        self.jn_x = 640
        self.jn_y = 280
        
        self.callback = callback

        titulo = ("Incluir Produção")
        self.root = Style.criar_janela_flutuante(titulo, self.jn_x, self.jn_y)
        self.elementos_tela(self.root)
        self.root.mainloop()

    def voltar_pagina(self, root):
        root.destroy()

    def atualizar_pagina(self,i=0):
        self.root.destroy()
        self.dados = None
        if i == 1:
            from tela_estoque import Estoque
            Estoque.estoque_lista(self.callback)
            
    def opcaomenu(self, choice, opmenu_var):
        if choice is None:
            opmenu_var.set('Semente')
        self.semente_selecionada_id = choice
        
    def modificacao_producao(self,semente,qtd,tempo):
        msg_box = MessageBox()
        
        result = Access.cadastrarProducao(semente,qtd,tempo)
        if result:
            msg_box.showinfo_autoclose(f"Insumo cadastrado com sucesso!")
        else:
            msg_box.showinfo_autoclose(f"Insumo não cadastrado!")
        
        
        if result:
            self.atualizar_pagina(1)
    
    def elementos_tela(self, root):
        
        self.semente_selecionada_id = None
        list_sementes = Access.listarSementes()
        id_sementes = {"": None}
        nomes_sementes = [""]
        
        for i in list_sementes:
            id_sementes[i['nome']] = i['id']
            nomes_sementes.append(i['nome'])
            
        opmenu_var = ctk.StringVar(value='Escolha uma semente')
        insumos = ctk.CTkOptionMenu(root, width=620, height=35, values=nomes_sementes, variable=opmenu_var,
                                                command=lambda choice: self.opcaomenu(id_sementes[choice], opmenu_var),fg_color=Style.color('fg'))
        insumos.grid(row=1, column=0,columnspan=2, padx=10, pady=10)

        qtdinsumo = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Quantidade')
        qtdinsumo.grid(row=2,column=0,columnspan=2, padx=10, pady=10)

        tempoCultivo = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Tempo de Cultivo')
        tempoCultivo.grid(row=3,column=0,columnspan=2, padx=10, pady=10)

        btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.voltar_pagina(root),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
        btn_cancelar.grid(row=5, column=0, padx=10, pady=10)

        btn_cadastrar = ctk.CTkButton(root, width=300, height=35, text='Cadastrar',fg_color=Style.color('fg'),hover_color=Style.color('hover')
                                      ,command=lambda:self.modificacao_producao(self.semente_selecionada_id,qtdinsumo.get(),tempoCultivo.get()))
        btn_cadastrar.grid(row=5, column=1, padx=10, pady=10)
        
        