from tkinter import *
import customtkinter as ctk

from style import Style

class Relatorio:
    def __init__(self,root,main_instance):

        self.root = root
        self.main = main_instance
        self.frame= Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))

        cont_frame = Frame(self.frame, bg=Style.color('bg'))
        cont_frame.pack(fill="x", padx=10, pady=10)

        btn_voltar = ctk.CTkButton(cont_frame, text="", image=Style.img('img_icon_voltar'), font=Style.font_style(), width=20, height=20, corner_radius=10,
                                        command=self.show_telaAnterior, fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),
                                        border_width=3, border_color=Style.color('hover_2'))
        btn_voltar.pack(pady=5, padx=5, side=LEFT)

        pesq_label = ctk.CTkLabel(cont_frame, text="Selecione o Conteudo:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=5, side=LEFT)
        
        optionmenu_var = ctk.StringVar(value="Escolha o conteudo")
        list_cont = ["", "Produção", "Pedidos de Venda", "Pedidos de Compras"]
        self.cont = ctk.CTkOptionMenu(cont_frame, width=800, height=35, values=list_cont,variable=optionmenu_var, fg_color=Style.color('fg'))
        self.cont.pack(pady=5, padx=5, side=LEFT)

        btn_gerarRelatorio = ctk.CTkButton(cont_frame, text='Gerar Relatorio', font=('Arial', 15, 'bold'), corner_radius=3, width=150, height=40,
                                        fg_color=Style.color('fg'), hover_color=Style.color('hover'))
        btn_gerarRelatorio.pack(pady=5, padx=10, side=RIGHT)
        
        mostra_frame = Frame(self.frame, bg=Style.color('bg_frame'),width=1100, height=350)
        mostra_frame.pack(fill="both", expand=True, pady=10, padx=10)
        
    def show_telaAnterior(self):
        self.main.mostrar_tela("telaProducao")
        
    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()