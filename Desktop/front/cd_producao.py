import customtkinter as ctk # pip install customtkinter

from access import Access
from style import Style

class cdProducao:
    
    def __init__(self):
        self.jn_x = 640
        self.jn_y = 280

        titulo = ("Incluir Produção")
        self.root = Style.criar_janela_flutuante(titulo, self.jn_x, self.jn_y)
        self.elementos_tela(self.root)
        self.root.mainloop()

    def voltar_pagina(self, root):
        root.destroy()

    def elementos_tela(self, root):
        
        Access.listarProducao()
        list_sementes = Access.listarSementes()
        
        id_sementes = {"": None}
        nomes_sementes = [""]
        
        for i in list_sementes:
            id_sementes[i['nome']] = i['id']
            nomes_sementes.append(i['nome'])
            
        opmenu_var = ctk.StringVar(value='Escolha uma semente')
        insumos = ctk.CTkOptionMenu(root, width=620, height=35, values=nomes_sementes, variable=opmenu_var,fg_color=Style.color('fg'))
        insumos.grid(row=1, column=0,columnspan=2, padx=10, pady=10)

        nomeinsumo = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Quantidade')
        nomeinsumo.grid(row=2,column=0,columnspan=2, padx=10, pady=10)

        descinsumo = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Tempo de Cultivo')
        descinsumo.grid(row=3,column=0,columnspan=2, padx=10, pady=10)

        descinsumo = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Restam')
        descinsumo.grid(row=4,column=0,columnspan=2, padx=10, pady=10)

        btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.voltar_pagina(root),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
        btn_cancelar.grid(row=5, column=0, padx=10, pady=10)

        btn_cadastrar = ctk.CTkButton(root, width=300, height=35, text='Cadastrar',fg_color=Style.color('fg'),hover_color=Style.color('hover'),command=Access.cadastrarProducao)
        btn_cadastrar.grid(row=5, column=1, padx=10, pady=10)