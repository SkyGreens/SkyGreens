from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter

from cd_fornecedor import cdFornecedor
from lista_fornecedor import todosFornecedores
from access import Access

fg = "#3ab355"  # Cor para botões
hover = "#316133"  # Cor ao passar o mouse
bg = "#dfeedf"  # Cor de fundo

class telaFornecedor:
    
    def __init__(self, root):
        
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack(side=TOP)
        self.frame.configure(background=bg)

        pesquisar_frame = Frame(self.frame, bg=bg)
        pesquisar_frame.pack(fill="x", padx=10, pady=10)

        self.pesq_conteudo = StringVar()
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Fornecedor:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=1, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=600,height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>", self.fornecedor_lista)

        cadFornecedor_button = ctk.CTkButton(pesquisar_frame, text='Cadastrar Fornecedor', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                               fg_color=fg, hover_color=hover,command=lambda:cdFornecedor(self))
        cadFornecedor_button.pack(pady=5, padx=10, side=RIGHT)
        
        listFornecedor_button = ctk.CTkButton(pesquisar_frame, text='Lista Fornecedores', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                               fg_color=fg, hover_color=hover,command=lambda:todosFornecedores(self,self.root))
        listFornecedor_button.pack(pady=5, padx=10, side=RIGHT)

        # lista de fornecedores
        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350)
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Carrega a lista completa
        self.fornecedor_lista()
        
    def fornecedor_lista(self,id_mostrar=0):
        
        fornecedores = Access.listarFornecedores()
        
        termoPesq = self.pesq_conteudo.get().lower()
        
        # Limpar os fornecedores anteriores
        for self.widget in self.lista_frame.winfo_children():
            self.widget.destroy()
        
        for i in fornecedores:
            
            status = "Inativo" if i['status'] == False else "Ativo"
            
            if (status == "Ativo") and(
                termoPesq in i['id'].lower() or
                termoPesq in i['nome'].lower() or
                termoPesq in i['cnpj'].lower()):
                
                fornecedor_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                fornecedor_frame.pack(fill="x", padx=10, pady=5)
                
                insumo = "Sem Cadastro" if i['semente'] == '' else i['semente']
                
                fornecedor_label = ctk.CTkLabel(fornecedor_frame, 
                                                text=f"ID: {i['id']} - {i['nome']} - CNPJ: {i['cnpj']} - Endereço: {i['endereco']} - Insumo: {insumo} - Status: {status}", 
                                                font=("Arial", 14))
                fornecedor_label.pack(pady=5)
                
            elif id_mostrar == 1:
                fornecedor_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                fornecedor_frame.pack(fill="x", padx=10, pady=5)
                
                insumo = "Sem Cadastro" if i['semente'] == '' else i['semente']
                
                fornecedor_label = ctk.CTkLabel(fornecedor_frame, 
                                                text=f"ID: {i['id']} - {i['nome']} - CNPJ: {i['cnpj']} - Endereço: {i['endereco']} - Insumo: {insumo} - Status: {status}", 
                                                font=("Arial", 14))
                fornecedor_label.pack(pady=5)
            
        if not fornecedores:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Nenhum fornecedor encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)
        
    #função para abrir a tela clicada
    def mostrar(self):
        self.frame.pack()
        
    #esconder as outras telas
    def esconder(self):
        self.frame.pack_forget()