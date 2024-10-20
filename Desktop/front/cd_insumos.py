import customtkinter as ctk # pip install customtkinter

from style import Style
#from access import Access

class cdInsumos:
    def __init__(self):
        self.jn_x = 640
        self.jn_y = 180
        
        titulo = ("Cadastrar Insumo")
        self.root = Style.criar_janela_flutuante(titulo, self.jn_x, self.jn_y)
        self.elementos_tela(self.root)
        self.root.mainloop()

    def voltar_pagina(self, root):
        root.destroy()

    def elementos_tela(self, root):
    
        nomeinsumo = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Nome')
        nomeinsumo.grid(row=1,column=0,columnspan=2, padx=10, pady=10)

        descinsumo = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Descrição')
        descinsumo.grid(row=2,column=0,columnspan=2, padx=10, pady=10)
        
        btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.voltar_pagina(root),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
        btn_cancelar.grid(row=5, column=0, padx=10, pady=10)

        btn_cadastrar = ctk.CTkButton(root, width=300, height=35, text='Cadastrar',fg_color=Style.color('fg'),hover_color=Style.color('hover'))
        btn_cadastrar.grid(row=5, column=1, padx=10, pady=10)