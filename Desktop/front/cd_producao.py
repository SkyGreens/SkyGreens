import customtkinter as ctk # pip install customtkinter
from tkinter import * # pip install tkinter

from style import Style
#from access import Access

class cdProducao:
    def __init__(self):
        jn_x = 640
        jn_y = 280
        root = Toplevel()
        root.title("Incluir Produção")
        root.geometry(f"{jn_x}x{jn_y}")
        root.wm_attributes('-toolwindow', 1)
        root.configure(background=Style.color('bg'))
        
        self.centralizar_janela(root, jn_x, jn_y)
        self.elementos_tela(root)
        root.maxsize(jn_x, jn_y)
        root.minsize(jn_x, jn_y)
        root.mainloop()

    def centralizar_janela(self,root, largura, altura):

        tela_largura = root.winfo_screenwidth()
        tela_altura = root.winfo_screenheight()

        x = (tela_largura // 2) - (largura // 2)
        y = (tela_altura // 2) - (altura // 2)

        root.geometry(f"{largura}x{altura}+{x}+{y}")

    def voltar_pagina(self, root):
        root.destroy()

    def elementos_tela(self, root):
        
        list_cargos = ["","Tomate", "Alecrim", "Alface"]
        opmenu_var = ctk.StringVar(value='Escolha uma semente')
        insumos = ctk.CTkOptionMenu(root, width=620, height=35, values=list_cargos, variable=opmenu_var,fg_color=Style.color('fg'))
        insumos.grid(row=1, column=0,columnspan=2, padx=10, pady=10)

        nomeinsumo = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Quantidade')
        nomeinsumo.grid(row=2,column=0,columnspan=2, padx=10, pady=10)

        descinsumo = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Tempo de Cultivo')
        descinsumo.grid(row=3,column=0,columnspan=2, padx=10, pady=10)

        descinsumo = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Restam')
        descinsumo.grid(row=4,column=0,columnspan=2, padx=10, pady=10)

        btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.voltar_pagina(root),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
        btn_cancelar.grid(row=5, column=0, padx=10, pady=10)

        btn_cadastrar = ctk.CTkButton(root, width=300, height=35, text='Cadastrar',fg_color=Style.color('fg'),hover_color=Style.color('hover'))
        btn_cadastrar.grid(row=5, column=1, padx=10, pady=10)