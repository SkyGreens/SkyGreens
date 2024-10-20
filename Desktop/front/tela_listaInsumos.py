from tkinter import *
import customtkinter as ctk

from style import Style
from cd_pedido import cdPedido

class listaInsumos:
    def __init__(self,root,main_instance):

        self.root = root
        self.main = main_instance
        self.frame= Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))

        btn_frame = Frame(self.frame, bg=Style.color('bg'))
        btn_frame.pack(fill="x", padx=0, pady=30)

        btn_pedidoCompra = ctk.CTkButton(btn_frame, text="Voltar",font=Style.font_style(),text_color='black', width=30, height=30, corner_radius=10,
                                         command=self.show_telaAnterior,fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),border_width=3,border_color=Style.color('hover_2'))
        btn_pedidoCompra.pack(pady=10,padx=5,side=LEFT)
        
    def show_telaAnterior(self):
        self.main.mostrar_tela("telaProducao")
        
    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()