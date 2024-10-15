from tkinter import * # pip install tkinter
import customtkinter as ctk # pip install customtkinter

from lista_insumos import listaInsumos
from relatorio import relatorio
from cd_producao import cdProducao

fg = "#316133"  # Cor para botões
hover = "#5d732f"  # Cor ao passar o mouse
bg = "#D9D9D9"  # Cor de fundo

class telaProducao:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=bg)


        pesquisar_frame = Frame(self.frame, bg=bg)
        pesquisar_frame.pack(fill="x", padx=10, pady=10)

        btn_listaInsumos = ctk.CTkButton(pesquisar_frame, text='Insumos', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                               fg_color=fg, hover_color=hover,command=listaInsumos)
        btn_listaInsumos.pack(pady=5, padx=10, side=LEFT)

        btn_gerarRelatorio = ctk.CTkButton(pesquisar_frame, text='Relatorio', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                               fg_color=fg, hover_color=hover,command=relatorio)
        btn_gerarRelatorio.pack(pady=5, padx=10, side=LEFT)

        btn_cadastrarPrateleira = ctk.CTkButton(pesquisar_frame, text='Incluir Produção', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                               fg_color=fg, hover_color=hover, command=cdProducao)
        btn_cadastrarPrateleira.pack(pady=5, padx=10, side=RIGHT)
       

    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()