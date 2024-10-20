from tkinter import *
import customtkinter as ctk

from style import Style
from cd_producao import cdProducao

class telaProducao:
    def __init__(self, root,main_app):
        self.root = root
        self.main_app = main_app
        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))

        btn_frame = Frame(self.frame, bg=Style.color('bg'))
        btn_frame.pack(fill="x", padx=0, side=TOP)

        btn_relatorio = ctk.CTkButton(btn_frame, text="Relatório",font=Style.font_style(),text_color='black',image=Style.img('img_icon_relatorio')
                                      ,compound=TOP, width=280, height=50, corner_radius=10,fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),
                                      command=lambda:self.verificar("Relatorio"),border_width=3,border_color=Style.color('hover_2'))
        btn_relatorio.grid(row=0, column=0, padx=10, pady=10)
        

        btn_estoque = ctk.CTkButton(btn_frame, text="Estoque",font=Style.font_style(),text_color='black',image=Style.img('img_icon_estoque')
                                    ,compound=TOP, width=280, height=50, corner_radius=10,fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),
                                    command=lambda:self.verificar("Estoque"),border_width=3,border_color=Style.color('hover_2'))
        btn_estoque.grid(row=0, column=1, padx=10, pady=10)


        btn_insumos = ctk.CTkButton(btn_frame, text="Insumos",font=Style.font_style(),text_color='black',image=Style.img('img_icon_insumos')
                                    ,compound=TOP, width=280, height=50, corner_radius=10,fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),
                                    command=lambda:self.verificar("listaInsumos"),border_width=3,border_color=Style.color('hover_2'))
        btn_insumos.grid(row=0, column=2, padx=10, pady=10)


        btn_producao = ctk.CTkButton(btn_frame, text="Incluir Produção",font=Style.font_style(),image=Style.img('img_icon_producao')
                                     ,compound=TOP,text_color='black', width=280, height=50, corner_radius=10,fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'), 
                                     command=cdProducao,border_width=3,border_color=Style.color('hover_2'))
        btn_producao.grid(row=0, column=3, padx=10, pady=10)

        cards_frame = ctk.CTkScrollableFrame(self.frame,orientation="horizontal", width=200, height=400,fg_color=Style.color('bg'))
        cards_frame.pack(fill="x", expand=True, side=TOP)
        
        
        semente = "Espinafre"
        codigo = "5501"
        status = "Disponivel"
        quantidade = 99
        tempo_cultivo = 30
        dias_restantes = 10
        
        def centro_lb(valor):
            label_x = (260 - valor.winfo_reqwidth()) // 2 
            label_y = (40 - valor.winfo_reqheight()) // 2 
            valor.place(x=label_x, y=label_y)
            
        for i in range(0, 5):
            card = f"card{i}"
            card = ctk.CTkFrame(cards_frame, width=280, height=340, corner_radius=10, 
                                fg_color=Style.color('fg_2'), border_width=3, 
                                border_color=Style.color('hover_2'))
            card.grid(row=1, column=i, padx=10, pady=10)
            

            lb_semente = ctk.CTkLabel(card, text=f"{semente}", text_color="black", font=Style.font_style())
            lb_semente.place(x=10, y=10)
            
            btn_editar = ctk.CTkButton(card, text='',image=Style.img('img_icon_edit'),  width=10,height=10,fg_color=Style.color('fg'),hover_color=Style.color('hover'))
            btn_editar.place(x=230, y=10)

            lb_codigo = ctk.CTkLabel(card, text=f"Código: {codigo}", text_color="black", font=Style.font_style())
            lb_codigo.place(x=10, y=35)

            lb_status = ctk.CTkLabel(card, text=f"{status}", text_color="black", font=Style.font_style())
            lb_status.place(x=10, y=60)

            # ===

            lbt_qtd = ctk.CTkLabel(card, text="Quantidade", text_color="black", font=Style.font_style())
            lbt_qtd.place(x=10, y=110)

            qtd_frame = ctk.CTkFrame(card, corner_radius=10, fg_color=Style.color('bg'), border_color=Style.color('hover_2'), width=260, height=40)
            qtd_frame.place(x=10, y=140)

            lbv_qtd = ctk.CTkLabel(qtd_frame, text=f"{quantidade}", text_color="black", font=Style.font_style())
            centro_lb(lbv_qtd)
            
            lb_tempoc = ctk.CTkLabel(card, text=f"Dias de Cultivo", text_color="black", font=Style.font_style())
            lb_tempoc.place(x=10, y=180)
            
            tempoc_frame = ctk.CTkFrame(card, corner_radius=10, fg_color=Style.color('bg'), border_color=Style.color('hover_2'), width=260, height=40)
            tempoc_frame.place(x=10, y=210)

            lbv_tempoc = ctk.CTkLabel(tempoc_frame, text=f"{tempo_cultivo}", text_color="black", font=Style.font_style())
            centro_lb(lbv_tempoc)
            
            lb_diasr = ctk.CTkLabel(card, text=f"Dias Restantes", text_color="black", font=Style.font_style())
            lb_diasr.place(x=10, y=252)
            
            tempor_frame = ctk.CTkFrame(card, corner_radius=10, fg_color=Style.color('bg'), border_color=Style.color('hover_2'), width=260, height=40)
            tempor_frame.place(x=10, y=282)

            lbv_tempor = ctk.CTkLabel(tempor_frame, text=f"{dias_restantes}", text_color="black", font=Style.font_style())
            centro_lb(lbv_tempor)

    def verificar(self, n):
        self.mostrar_tela(n)
        self.esconder()
    
    def mostrar_tela(self, tela_nome):
        self.main_app.mostrar_tela(tela_nome)
    
    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()