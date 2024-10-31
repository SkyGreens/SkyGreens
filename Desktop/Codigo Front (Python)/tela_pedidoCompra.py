from tkinter import *
import customtkinter as ctk

from style import Style,MessageBox
from cd_pedido import cdPedido
from access import Access

class pedidoCompra:
    def __init__(self,root,main_instance):

        self.root = root
        self.main = main_instance
        self.message_box = MessageBox()
        self.frame= Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))

        pesquisar_frame = Frame(self.frame, bg=Style.color('bg'))
        pesquisar_frame.pack(fill="x", padx=10, pady=10)

        btn_voltar = ctk.CTkButton(pesquisar_frame, text="", image=Style.img('img_icon_voltar'), font=Style.font_style(), width=20, height=20, corner_radius=10,
                                        command=self.show_telaAnterior, fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),
                                        border_width=3, border_color=Style.color('hover_2'))
        btn_voltar.pack(pady=5, padx=5, side=LEFT)

        self.pesq_conteudo = StringVar()
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Compra:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=5, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=800, height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>")

        btn_cdInsumo = ctk.CTkButton(pesquisar_frame, text='Cadastrar Compra', font=('Arial', 15, 'bold'), corner_radius=3, width=150, height=40,
                                        fg_color=Style.color('fg'), hover_color=Style.color('hover'), command=self.modificar_pedido)
        btn_cdInsumo.pack(pady=5, padx=10, side=RIGHT)

        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350, fg_color=Style.color('bg_frame'))
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)
        
    def modificar_pedido(self):
        result = Access.verificar_permissoes(self,0)
        if result:
            cdPedido()
        else:
            result = self.message_box.showerror("Autenticação","Acesso não autorizado!")
            
    def show_telaAnterior(self):
        self.main.mostrar_tela("telaPedidos")
        
    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()