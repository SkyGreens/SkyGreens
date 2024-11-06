from tkinter import *
import customtkinter as ctk

from style import Style
from access import Access

class Estoque:
    
    def __init__(self,root,main_instance):

        self.root = root
        self.main = main_instance
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
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Estoque:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=5, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=800, height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>",self.estoque_lista)

        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350, fg_color=Style.color('bg_frame'))
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)
        
        self.estoque_lista()

    def estoque_lista(self,event=None):
        estoque = Access.listarEstoque()
       
        termoPesq = self.pesq_conteudo.get().lower()
        
        for widget in self.lista_frame.winfo_children():
            widget.destroy()
        
        for i in estoque:
            if (termoPesq in i['nome_semente'].lower()):
                
                est_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                est_frame.pack(fill="x", padx=10, pady=5)
                
                lb_est = ctk.CTkLabel(est_frame, text=f"ID: {i['id']} | Nome: {i['nome_semente']} | Descrição {i['desc']} | Quantidade: {i['qtd']}", font=("Arial", 14))
                lb_est.pack(side="left",pady=5)
                
                
        if not estoque:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Estoque não encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)
    
    def show_telaAnterior(self):
        self.main.mostrar_tela("telaProducao")
        
    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()