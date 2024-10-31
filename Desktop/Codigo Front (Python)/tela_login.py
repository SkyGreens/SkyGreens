from tkinter import *  # pip install tkinter
import customtkinter as ctk  # pip install customtkinter
from tkinter import messagebox  # pip install tkinter

from style import Style
from access import Access

class telaLogin:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.janela_login()
    
    def janela_login(self):
        ctk.set_appearance_mode("light")
        
        self.frame = ctk.CTkFrame(master=self.root, width=300, height=400,fg_color=Style.color('bg_frame'))
        self.frame.pack(expand=True, padx=20, pady=20)

        lb_titulo = ctk.CTkLabel(master=self.frame, text="Acesse sua conta", font=("Arial", 30, "bold"))
        lb_titulo.pack(pady=(20, 10))

        lb_subtitulo = ctk.CTkLabel(master=self.frame, text="Sua contribuição é essencial! Entre para colaborar conosco!", font=("Arial", 12))
        lb_subtitulo.pack(pady=(0, 20))
        
        en_nome = ctk.CTkEntry(self.frame, placeholder_text="Usuário", width=400, height=35)
        en_nome.pack(pady=(0, 10), padx=20)

        en_senha = ctk.CTkEntry(self.frame, placeholder_text="Senha", show="*", width=400, height=35)
        en_senha.pack(pady=(0, 10), padx=20)
        
        lb_separador = ctk.CTkLabel(master=self.frame, text=37 * "-" + " ou " + 37 * "-", font=("Arial", 12))
        lb_separador.pack(pady=5)

        bt_esqsenha = ctk.CTkButton(master=self.frame, text="Esqueceu a senha?", width=50, height=10, fg_color=Style.color('fg'), hover_color=Style.color('hover'))
        bt_esqsenha.pack(pady=5)

        bt_ok = ctk.CTkButton(self.frame, text="Entrar", font=('Arial', 15, 'bold'), corner_radius=3, fg_color=Style.color('fg'), hover_color=Style.color('hover'),
                              command=lambda: self.verificar_login(en_nome.get(), en_senha.get()), width=250, height=35)
        bt_ok.pack(pady=20)

    def verificar_login(self, user, senha):
        user = 12345678909
        senha = "admin"
        
        #user = 45242561807
        #senha = 'gerente'
        
        #user = '01800980809'
        #senha = 'assistente'
        
        self.frame.destroy()
        access = Access.login(user, senha, self.app)    
        
        if access:
            messagebox.showinfo(title="Erro", message="Login falhou: Usuário ou senha inválidos")
