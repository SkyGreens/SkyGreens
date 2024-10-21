from tkinter import * # pip install tkinter
import customtkinter as ctk # pip install customtkinter

from cd_usuario import cdUsuario 
from access import Access
from style import Style

class telaUsuarios:
    
    def __init__(self,root):

        self.root=root
        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))

        pesquisar_frame = Frame(self.frame, bg=Style.color('bg'))
        pesquisar_frame.pack(fill="x", padx=10, pady=10)

        self.pesq_conteudo = StringVar()
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Usuário:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=1, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=800,height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>", self.usuario_lista)

        btn_cadastrarUser = ctk.CTkButton(pesquisar_frame, text='Cadastrar Usuário', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                               fg_color=Style.color('fg'), hover_color=Style.color('hover'),command=lambda:cdUsuario(self))
        btn_cadastrarUser.pack(pady=5, padx=10, side=RIGHT)

        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350,fg_color=Style.color('bg_frame'))
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)

        self.usuario_lista()
        
    def excluir_usuario(self,dados):
        iduser = dados['id']
        result = Access.excluirUsuario(iduser)
        
        if result:
            self.usuario_lista()
            
    def usuario_lista(self,event=None):
        
        usuarios = Access.listarUsuarios()
        termoPesq = self.pesq_conteudo.get().lower()
        
        # Limpar os fornecedores anteriores
        for widget in self.lista_frame.winfo_children():
            widget.destroy()
        
        cargo_map = {"ADMIN": "Administrador","GERENTEPRODUCAO": "Gerente de Produção","ASSISTENTEPRODUCAO": "Assistente de Produção"}
        
        # Exibir fornecedores correspondentes à pesquisa
        for i in usuarios:
            if (termoPesq in i['cpf'].lower() or
                termoPesq in i['nome'].lower() or
                termoPesq in i['cargo'].lower()):
                
                user_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                user_frame.pack(fill="x", padx=10, pady=5)
                
                cargo_visual = cargo_map.get(i['cargo'])

                user_label = ctk.CTkLabel(user_frame, text=f"Nome: {i['nome']} | Cargo: {cargo_visual}", font=("Arial", 14))
                user_label.pack(side="left",pady=5)
                
                btn_editar = ctk.CTkButton(user_frame, text='',image=Style.img('img_icon_edit'),  width=30,height=30, command=lambda dados=i: self.abrir_tela(dados,1),fg_color=Style.color('fg'),hover_color=Style.color('hover'))
                btn_editar.pack(side="right", padx=5, pady=5)
                
                btn_excluir = ctk.CTkButton(user_frame, width=30, height=30, text='',image=Style.img('img_icon_delete'),command = lambda dados=i: self.excluir_usuario(dados), fg_color=Style.color('fg_red'), hover_color=Style.color('hover_red'))
                btn_excluir.pack(side="right", padx=5, pady=5)
                
                user_label.bind("<Button-1>", lambda e, dados=i: self.abrir_tela(dados,0))
                
        if not usuarios:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Nenhum usuário encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)

    def abrir_tela(self, dados,n):
        cdUsuario(self, dados=dados,editar=n)
    
    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()