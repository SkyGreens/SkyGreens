from tkinter import *
import customtkinter as ctk

from style import Style

class telaPedidos:
    def __init__(self,root,main_app):

        self.root = root
        self.main_app = main_app
        self.frame= Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))

        btn_frame = Frame(self.frame, bg=Style.color('bg'))
        btn_frame.pack(fill="x", padx=0, pady=30)

        btn_pedidoCompra = ctk.CTkButton(btn_frame, text="Pedidos de Compra",font=Style.font_style(),text_color='black',image=Style.img('img_icon_pedidoCompra'),
                                         compound=TOP, width=280, height=390, corner_radius=10,
                                         command=lambda:self.verificar("pedidoCompra"), fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),border_width=3,border_color=Style.color('hover_2'))
        
        btn_pedidoCompra.grid(row=0, column=0, padx=10, pady=10)
        
        btn_pedidoVenda = ctk.CTkButton(btn_frame, text="Pedidos de Venda",font=Style.font_style(),text_color='black',image=Style.img('img_icon_pedidoVenda'),
                                        compound=TOP, width=280, height=390, corner_radius=10,
                                        command=lambda:self.verificar("pedidoVenda"),fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),border_width=3,border_color=Style.color('hover_2'))
        
        btn_pedidoVenda.grid(row=0, column=1, padx=10, pady=10)

    def verificar(self, n):
        self.mostrar_tela(n)
        self.esconder()
    
    def mostrar_tela(self, tela_nome):
        self.main_app.mostrar_tela(tela_nome)
    
    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget() 

