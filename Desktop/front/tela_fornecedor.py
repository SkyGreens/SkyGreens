from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter

from cd_fornecedor import cdFornecedor

fg = "#3ab355"  # Cor para botões
hover = "#316133"  # Cor ao passar o mouse
bg = "#dfeedf"  # Cor de fundo

fornecedores = [
    {"nome": "Flávio Waltz Corporation", "cnpj": "24.995.561/0001-82", "endereço": "Rua 1, São Paulo"},
    {"nome": "Empresa Alimentos Verde", "cnpj": "10.256.478/0001-30", "endereço": "Rua 2, Curitiba"},
    {"nome": "Coop. Agropecuária União", "cnpj": "85.478.213/0001-96", "endereço": "Rua 3, Belo Horizonte"},
    {"nome": "Grãos do Brasil Ltda", "cnpj": "36.547.895/0001-22", "endereço": "Rua 4, Rio de Janeiro"},
    {"nome": "Orgânicos Sabor Vida", "cnpj": "27.854.236/0001-89", "endereço": "Rua 5, Porto Alegre"},
    {"nome": "Orgânicos Sabor Vida", "cnpj": "27.854.236/0001-89", "endereço": "Rua 5, Porto Alegre"},
    {"nome": "Orgânicos Sabor Vida", "cnpj": "27.854.236/0001-89", "endereço": "Rua 5, Porto Alegre"},
    {"nome": "Orgânicos Sabor Vida", "cnpj": "27.854.236/0001-89", "endereço": "Rua 5, Porto Alegre"}
]

class telaFornecedor:
    
    def __init__(self, root, controller):
        
        self.root = root
        self.controller = controller
        self.frame = Frame(self.root)
        self.frame.pack(side=TOP)
        self.frame.configure(background=bg)

        pesquisar_frame = Frame(self.frame, bg=bg)
        pesquisar_frame.pack(fill="x", padx=10, pady=10)

        # Barra de Pesquisa
        self.pesq_conteudo = StringVar()
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Fornecedor:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=1, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=600,height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>", self.fornecedor_lista)

        
        listFornecedor_button = ctk.CTkButton(pesquisar_frame, text='Cadastrar Fornecedor', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                               fg_color=fg, hover_color=hover,command=lambda:cdFornecedor())
        listFornecedor_button.pack(pady=5, padx=10, side=RIGHT)
        
        cadFornecedor_button = ctk.CTkButton(pesquisar_frame, text='Lista Fornecedor', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                               fg_color=fg, hover_color=hover)
        cadFornecedor_button.pack(pady=5, padx=10, side=RIGHT)

        # lista de fornecedores
        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350)
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Carrega a lista completa
        self.fornecedor_lista()

    def fornecedor_lista(self, event=None):
        
        # Limpar os fornecedores anteriores
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        termoPesq = self.pesq_conteudo.get().lower()

        # Exibir fornecedores correspondentes à pesquisa
        for i in fornecedores:
            if (termoPesq in i['nome'].lower() or
                termoPesq in i['cnpj'].lower() or
                termoPesq in i['endereço'].lower()):
                
                fornecedor_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                fornecedor_frame.pack(fill="x", padx=10, pady=5)

                fornecedor_label = ctk.CTkLabel(fornecedor_frame, 
                                                text=f"{i['nome']} - CNPJ: {i['cnpj']} - Endereço: {i['endereço']}", 
                                                font=("Arial", 14))
                fornecedor_label.pack(pady=5)

    #função para abrir a tela clicada
    def mostrar(self):
        self.frame.pack()
        
    #esconder as outras telas
    def esconder(self):
        self.frame.pack_forget()