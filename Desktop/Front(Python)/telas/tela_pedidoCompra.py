from tkinter import *
import customtkinter as ctk

from style import Style,MessageBox
from janelas.cd_pedidoCompra import cdPedidoCompra
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
        self.pesq_entry.bind("<KeyRelease>", self.compras_lista)

        btn_cdInsumo = ctk.CTkButton(pesquisar_frame, text='Cadastrar Compra', font=('Arial', 15, 'bold'), corner_radius=3, width=150, height=40,
                                        fg_color=Style.color('fg'), hover_color=Style.color('hover'), command=lambda:self.modificar_pedido(self))
        btn_cdInsumo.pack(pady=5, padx=10, side=RIGHT)

        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350, fg_color=Style.color('bg_frame'))
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)
        
        self.compras_lista()
            
    def compras_lista(self,event=None):
        compras = Access.listarpedidosCompra()
        termoPesq = self.pesq_conteudo.get().lower()
        
        for widget in self.lista_frame.winfo_children():
            widget.destroy()
        
        for i in compras:
            if (termoPesq in i['fornecedor']['razaoSocial'].lower() or
                termoPesq in i['semente']['nome'].lower()):
                
                compra_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                compra_frame.pack(fill="x", padx=10, pady=5)

                compra_label = ctk.CTkLabel(compra_frame, text=f"Fornecedor: {i['fornecedor']['razaoSocial']} | Quantidade: {i['qtd']} | Semente: {i['semente']['nome']}", font=("Arial", 14))
                compra_label.pack(side="left",pady=5)
                
                compra_label.bind("<Button-1>", lambda e, dados=i: self.abrir_tela_edicao(dados,0))
                
        if not compras:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Nenhum pedido de compra encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)
    
    def abrir_tela_edicao(self, dados,n):
        cdPedidoCompra(self, dados=dados,editar=n)
            
    def modificar_pedido(self, callback):
        result = Access.verificar_permissoes(self,0)
        if result:
            cdPedidoCompra(callback)
        else:
            result = self.message_box.showerror("Autenticação","Acesso não autorizado!")
            
    def show_telaAnterior(self):
        self.main.mostrar_tela("telaPedidos",5)
        
    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()