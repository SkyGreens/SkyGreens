from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter
from tkinter import messagebox #pip install tkinter

from access import Access

fg = "#3ab355"  # Cor para botões
hover = "#316133"  # Cor ao passar o mouse
bg = "#dfeedf"  # Cor de fundo

class telaLogin:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.janela_login()
    
    def janela_login(self):
        
        ctk.set_appearance_mode("light")
        
        self.frame = ctk.CTkFrame(master=self.root, width=200, height=250)
        self.frame.pack(expand=True, fill="both")
        
         #==Componentes
        lb_titulo = ctk.CTkLabel(master=self.frame, text="Acesse sua conta", font=("Arial", 35, "bold"))
        lb_titulo.pack(pady=30)

        lb_subtitulo = ctk.CTkLabel(master=self.frame, text="Sua contribuição é essencial! Entre para colaborar conosco!", font=("Arial", 16))
        lb_subtitulo.pack(pady=0)

        en_nome = ctk.CTkEntry(self.frame,placeholder_text="Usuário",width=400,height=35)
        en_nome.pack(pady=10)
        
        en_senha = ctk.CTkEntry(self.frame,placeholder_text="Senha",show = "*",width=400,height=35)
        en_senha.pack(pady=10)

        lb_subtitulo = ctk.CTkLabel(master=self.frame, text=37*"-"+"ou"+37*"-", font=("Arial", 16))
        lb_subtitulo.pack()

        bt_esqsenha = ctk.CTkButton(master=self.frame, text="Esqueceu a senha?", width=50,height=10, fg_color=fg, hover_color=hover)
        bt_esqsenha.pack()
        
        bt_ok = ctk.CTkButton(self.frame,text="Ok",font=('Arial',15,'bold'),corner_radius=3,fg_color=fg,hover_color=hover
                                , command=lambda: self.verificar_login(en_nome.get(),en_senha.get()),width=400,height=35)
        bt_ok.pack(pady=10)

    def verificar_login(self, user, senha):
        user = 12345678909
        senha = "admin"
        
        self.frame.destroy()
        access = Access.login(user, senha, self.app)    
        
        if access:
            messagebox.showinfo(title="Erro",message="Login falhou: Usuário ou senha inválidos")



