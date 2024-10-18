from tkinter import *
import customtkinter as ctk

from style import Style

from lista_insumos import listaInsumos
from relatorio import relatorio
from cd_producao import cdProducao
from estoque import Estoque

class telaProducao:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))

        btn_frame = Frame(self.frame, bg=Style.color('bg'))
        btn_frame.pack(fill="x", padx=0, side=TOP)


        btn_relatorio = ctk.CTkButton(btn_frame, text="Relatório",font=Style.font_style(),text_color='black',image=Style.img('img_icon_relatorio')
                                      ,compound=TOP, width=280, height=50, corner_radius=10,fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),
                                      command=relatorio,border_width=3,border_color=Style.color('hover_2'))
        btn_relatorio.grid(row=0, column=0, padx=10, pady=10)
        

        btn_estoque = ctk.CTkButton(btn_frame, text="Estoque",font=Style.font_style(),text_color='black',image=Style.img('img_icon_estoque')
                                    ,compound=TOP, width=280, height=50, corner_radius=10,fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),
                                    command=Estoque,border_width=3,border_color=Style.color('hover_2'))
        btn_estoque.grid(row=0, column=1, padx=10, pady=10)


        btn_insumos = ctk.CTkButton(btn_frame, text="Insumos",font=Style.font_style(),text_color='black',image=Style.img('img_icon_insumos')
                                    ,compound=TOP, width=280, height=50, corner_radius=10,fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),
                                    command=listaInsumos,border_width=3,border_color=Style.color('hover_2'))
        btn_insumos.grid(row=0, column=2, padx=10, pady=10)


        btn_producao = ctk.CTkButton(btn_frame, text="Incluir Produção",font=Style.font_style(),image=Style.img('img_icon_producao')
                                     ,compound=TOP,text_color='black', width=280, height=50, corner_radius=10,fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'), 
                                     command=cdProducao,border_width=3,border_color=Style.color('hover_2'))
        btn_producao.grid(row=0, column=3, padx=10, pady=10)

        cards_frame = ctk.CTkScrollableFrame(self.frame,orientation="horizontal", width=200, height=400,fg_color=Style.color('bg'))
        cards_frame.pack(fill="x", expand=True, side=TOP)
        
        #card
        semente = "Espinafre"
        codigo = "5501"
        prateleira = "1"
        status = "Produção"
        
        for i in range(0,5):

            card = f"card{i}"
            card = ctk.CTkFrame(cards_frame, width=280, height=340, corner_radius=10,fg_color=Style.color('fg_2'),border_width=3,border_color=Style.color('hover_2'))
            card.grid(row=1, column=i, padx=10, pady=10)

            label_prateleira = ctk.CTkLabel(card, text=f"{semente}",text_color="black", font=Style.font_style())
            label_prateleira.place(x=10, y=10)

            #label_codigo = ctk.CTkLabel(card, text=f"{codigo}",text_color="black", font=Style.font_style())
            #label_codigo.place(x=10, y=200)
            
            #label_semente = ctk.CTkLabel(card, text=f"{semente}",text_color="black", font=Style.font_style())
            #label_semente.place(x=10, y=240)
            
            #label_status = ctk.CTkLabel(card, text=f"Status: {status}...",text_color="black", font=Style.font_style())
            #label_status.place(x=10, y=280)

        

    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()