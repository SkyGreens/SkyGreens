from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter

from style import Style
from cd_fornecedor import cdFornecedor
from access import Access

class telaFornecedor:
    
    def __init__(self, root):
        
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack(side=TOP)
        self.frame.configure(background=Style.color('bg'))

        pesquisar_frame = Frame(self.frame, bg=Style.color('bg'))
        pesquisar_frame.pack(fill="x", padx=10, pady=10)

        self.pesq_conteudo = StringVar()
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Fornecedor:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=1, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=600,height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>", self.fornecedor_lista)

        cadFornecedor_button = ctk.CTkButton(pesquisar_frame, text='Cadastrar Fornecedor', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                               fg_color=Style.color('fg'), hover_color=Style.color('hover'),command=lambda:cdFornecedor(self))
        cadFornecedor_button.pack(pady=5, padx=10, side=RIGHT)
        
        def escolhanmenu(choice):
            self.fornecedor_lista(choice)
        
        optionmenu_var = ctk.StringVar(value="Ativo")
        values = ["Todos","Ativo","Inativo"]
        optionmenu = ctk.CTkOptionMenu(pesquisar_frame,values=values,variable=optionmenu_var, corner_radius=3, width=200, height=40,command=escolhanmenu,fg_color=Style.color('fg'))
        optionmenu.pack(pady=5, padx=10, side=RIGHT)

        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350,fg_color=Style.color('bg_frame'))
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Carrega a lista completa
        self.fornecedor_lista()
        
    def fornecedor_lista(self,op_status="Ativo",event=None):
        
        fornecedores = Access.listarFornecedores()
        
        termoPesq = self.pesq_conteudo.get().lower()
        
        # Limpar os fornecedores anteriores
        for self.widget in self.lista_frame.winfo_children():
            self.widget.destroy()
        
        for i in fornecedores:
            
            status = "Inativo" if i['status'] == False else "Ativo"
            
            if (status == op_status) and(
                termoPesq in i['id'].lower() or
                termoPesq in i['nome'].lower() or
                termoPesq in i['cnpj'].lower()):
                
                fornecedor_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                fornecedor_frame.pack(fill="x", padx=10, pady=5)
                
                insumo = "Sem Cadastro" if i['semente'] == '' else i['semente']
                
                fornecedor_label = ctk.CTkLabel(fornecedor_frame, 
                                                text=f"ID: {i['id']} - {i['nome']} - CNPJ: {i['cnpj']} - Endereço: {i['endereco']} - Insumo: {insumo} - Status: {status}", 
                                                font=("Arial", 14))
                fornecedor_label.pack(side="left", pady=5)
                
                btn_editar = ctk.CTkButton(fornecedor_frame, text="Editar",  width=30,height=30, command=lambda dados=i: self.abrir_tela_edicao(dados),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
                btn_editar.pack(side="right", padx=5, pady=5)
                
                fornecedor_label.bind("<Button-1>", lambda e, dados=i: self.abrir_tela_edicao(dados))
                
            elif op_status == "Todos":
                fornecedor_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                fornecedor_frame.pack(fill="x", padx=10, pady=5)
                
                insumo = "Sem Cadastro" if i['semente'] == '' else i['semente']
                
                fornecedor_label = ctk.CTkLabel(fornecedor_frame, 
                                                text=f"ID: {i['id']} - {i['nome']} - CNPJ: {i['cnpj']} - Endereço: {i['endereco']} - Insumo: {insumo} - Status: {status}", 
                                                font=("Arial", 14))
                fornecedor_label.pack(side="left", pady=5)
                
                btn_editar = ctk.CTkButton(fornecedor_frame, text="Editar",  width=30,height=30, command=lambda dados=i: self.abrir_tela_edicao(dados),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
                btn_editar.pack(side="right", padx=5, pady=5)
                
                fornecedor_label.bind("<Button-1>", lambda e, dados=i: self.abrir_tela_edicao(dados))
            
        if not fornecedores:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Nenhum fornecedor encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)
            
    def abrir_tela_edicao(self, dados):
        cdFornecedor(self, dados=dados,editar=True)

    #função para abrir a tela clicada
    def mostrar(self):
        self.frame.pack()
        
    #esconder as outras telas
    def esconder(self):
        self.frame.pack_forget()