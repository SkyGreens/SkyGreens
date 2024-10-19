from tkinter import *  # pip install tkinter
import customtkinter as ctk  # pip install customtkinter

from style import Style
from cd_pedido import cdPedido 

class telaPedidos:
    
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))

        # Frame de pesquisa de pedidos
        pesquisar_frame = Frame(self.frame, bg=Style.color('bg'))
        pesquisar_frame.pack(fill="x", padx=10, pady=10)

        self.pesq_conteudo = StringVar()
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Pedido:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=1, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=800, height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>", self.pedido_lista)

        # Botão para abrir a tela de cadastrar pedidos
        btn_cadastrarPedido = ctk.CTkButton(pesquisar_frame, text='Cadastrar Pedido', font=('Arial', 15, 'bold'),
                                            corner_radius=3, width=100, height=40, fg_color=Style.color('fg'), 
                                            hover_color=Style.color('hover'), command=cdPedido)
        btn_cadastrarPedido.pack(pady=5, padx=10, side=RIGHT)

        # Frame de lista de pedidos
        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350, fg_color=Style.color('bg_frame'))
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Carregar a lista de pedidos
        self.pedido_lista()

    def pedido_lista(self, event=None):
        pedidos = [{"id":"000021","cliente":"Carlinhos da Pamonha","nome":"Alface","qtd":10},
                   {"id":"000315","cliente":"Zé da Pizza","nome":"Tomate","qtd":2},
                   {"id":"000561","cliente":"Maria Benedita Mercadin","nome":"Milho","qtd":25},
                   {"id":"000369","cliente":"Pamonha Mil Grau","nome":"Pocã","qtd":20},
                   {"id":"000456","cliente":"Tomate Cem","nome":"Banana","qtd":30},
                   {"id":"000159","cliente":"Mercadin Seu Jão","nome":"Maça","qtd":15}]

        # Limpar os pedidos anteriores
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        termoPesq = self.pesq_conteudo.get().lower()

        # Exibir pedidos correspondentes à pesquisa
        for i in pedidos:
            if (termoPesq in i['id'].lower() or
                termoPesq in i['nome'].lower() or
                termoPesq in i['quantidade'].lower()):
                
                pedido_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                pedido_frame.pack(fill="x", padx=10, pady=5)

                pedido_label = ctk.CTkLabel(pedido_frame, 
                                            text=f"{i['id']} | {i['cliente']} | {i['nome']} | Quantidade: {i['qtd']}", 
                                            font=("Arial", 14))
                pedido_label.pack(pady=5)

        if not pedidos:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Nenhum pedido encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)

    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()
