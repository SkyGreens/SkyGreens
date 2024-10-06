from tkinter import * # pip install tkinter
import customtkinter as ctk # pip install customtkinter

from cd_usuario import cdUsuario 

fg = "#3ab355"  # menu
hover = "#316133"  # hover/principal
bg = "#dfeedf"  # background

class telaUsuarios:
    
    def __init__(self,root,controller):

        self.root=root
        self.controller=controller
        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=bg)

        pesquisar_frame = Frame(self.frame, bg=bg)
        pesquisar_frame.pack(fill="x", padx=10, pady=10)

        self.pesq_conteudo = StringVar()
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Usuário:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=1, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=800,height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>", self.usuario_lista)

        
        btn_cadastrarUser = ctk.CTkButton(pesquisar_frame, text='Cadastrar Usuário', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                               fg_color=fg, hover_color=hover,command=lambda:cdUsuario())
        btn_cadastrarUser.pack(pady=5, padx=10, side=RIGHT)

        # lista de fornecedores
        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350)
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Carrega a lista completa
        self.usuario_lista()

    def usuario_lista(self, event=None):
        
        usuarios = [{"id":"1","nome":"Carlos Alberto","user":"carlos.alberto","cargo":"Gerente de Produção"},
                     {"id":"2","nome":"Carlos Alberto","user":"carlos.alberto","cargo":"Gerente de Administrador"},
                     {"id":"3","nome":"Carlos Alberto","user":"carlos.alberto","cargo":"Gerente"},
                     {"id":"4","nome":"Carlos Alberto","user":"carlos.alberto","cargo":"Assistente"},
                     {"id":"5","nome":"Carlos Alberto","user":"carlos.alberto","cargo":"Gerente de Produção"},
                     {"id":"6","nome":"Carlos Alberto","user":"carlos.alberto","cargo":"Gerente de Produção"},
                     {"id":"7","nome":"Carlos Alberto","user":"carlos.alberto","cargo":"Gerente de Produção"},
                     {"id":"8","nome":"Carlos Alberto","user":"carlos.alberto","cargo":"Gerente de Produção"},
                     {"id":"9","nome":"Carlos Alberto","cargo":"Gerente de Produção"}]
        
        # Limpar os fornecedores anteriores
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        termoPesq = self.pesq_conteudo.get().lower()
        
        # Exibir fornecedores correspondentes à pesquisa
        for i in usuarios:
            if (termoPesq in i['id'].lower() or
                termoPesq in i['nome'].lower() or
                termoPesq in i['cargo'].lower()):
                
                user_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                user_frame.pack(fill="x", padx=10, pady=5)

                user_label = ctk.CTkLabel(user_frame, 
                                                text=f"{i['id']} - {i['nome']} - Cargo: {i['cargo']}", 
                                                font=("Arial", 14))
                user_label.pack(pady=5)
                
        if not usuarios:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Nenhum usuário encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)


    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()
