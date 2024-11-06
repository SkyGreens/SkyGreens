from tkinter import *
import customtkinter as ctk

from style import Style,MessageBox
from cd_insumos import cdInsumos
from access import Access

class listaInsumos:
    
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
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Insumo:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=5, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=800, height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>",self.sementes_lista)

        btn_cdInsumo = ctk.CTkButton(pesquisar_frame, text='Cadastrar Insumo', font=('Arial', 15, 'bold'), corner_radius=3, width=150, height=40,
                                        fg_color=Style.color('fg'), hover_color=Style.color('hover'), command=lambda: self.modificar_insumos(self))
        btn_cdInsumo.pack(pady=5, padx=10, side=RIGHT)

        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350, fg_color=Style.color('bg_frame'))
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)
        
        self.sementes_lista()
        
    def modificar_insumos(self,callback):
        result = Access.verificar_permissoes(self,0)
        if result:
            cdInsumos(callback)
        else:
            result = self.message_box.showerror("Autenticação","Acesso não autorizado!")
        
    def sementes_lista(self,event=None):
        result = Access.verificar_permissoes(self,0)
        sementes = Access.listarSementes()
        termoPesq = self.pesq_conteudo.get().lower()
        
        for widget in self.lista_frame.winfo_children():
            widget.destroy()
        
        for i in sementes:
            if (termoPesq in str(i['id']) or
                termoPesq in i['nome'].lower()):
                
                sem_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                sem_frame.pack(fill="x", padx=10, pady=5)
                
                lb_sem = ctk.CTkLabel(sem_frame, text=f"ID: {i['id']} | {i['nome']}", font=("Arial", 14))
                lb_sem.pack(side="left",pady=5)
                
                if result:
                    btn_editar = ctk.CTkButton(sem_frame, text='',image=Style.img('img_icon_edit'),  width=30,height=30,fg_color=Style.color('fg'),hover_color=Style.color('hover'))
                    btn_editar.pack(side="right", padx=5, pady=5)
                    
                    btn_excluir = ctk.CTkButton(sem_frame, width=30, height=30, text='',image=Style.img('img_icon_delete'), fg_color=Style.color('fg_red'), hover_color=Style.color('hover_red'))
                    btn_excluir.pack(side="right", padx=5, pady=5)
                
                lb_sem.bind("<Button-1>", lambda e, dados=i: self.abrir_tela(dados,0))
                
        if not sementes:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Nenhum Insumo Cadastrado.", font=("Arial", 14))
            msg_label.pack(pady=5)
    
    def show_telaAnterior(self):
        self.main.mostrar_tela("telaProducao")
    
    def abrir_tela(self, dados,n):
        cdInsumos(self, dados=dados,editar=n)
        
    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()