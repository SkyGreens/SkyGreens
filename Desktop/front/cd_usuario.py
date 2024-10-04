import customtkinter as ctk # pip install customtkinter
from tkinter import Toplevel # pip install tkinter
import random

#from access import Access

fg = "#3ab355"  # menu
hover = "#316133"  # hover/principal
bg = "#dfeedf"  # background

class cdUsuario:
    def __init__(self):
        jn_x = 640
        jn_y = 300
        root = Toplevel()
        root.title("Cadastrar Usuário")
        root.geometry(f"{jn_x}x{jn_y}")
        root.wm_attributes('-toolwindow', 1)
        root.configure(background='#dfeedf')

        #ctk.set_appearance_mode("light")
        
        self.centralizar_janela(root, jn_x, jn_y)
        self.elementos_tela(root)
        root.maxsize(jn_x, jn_y)
        root.minsize(jn_x, jn_y)
        root.mainloop()

    def centralizar_janela(self,root, largura, altura):

        tela_largura = root.winfo_screenwidth()
        tela_altura = root.winfo_screenheight()

        x = (tela_largura // 2) - (largura // 2)
        y = (tela_altura // 2) - (altura // 2)

        root.geometry(f"{largura}x{altura}+{x}+{y}")
    
    def cadastrar_usuario(self,cpf,cargo, nome, status,email):
        status = False if status == "Inativo" else True

        sn_parte = str(random.randint(100,999)) #gera 3 numeros aleatorios para compor a senha
        senha = cpf[0:3]+sn_parte

        print(f"Usuário Cadastrado\nCPF: {cpf}\nNome: {nome}\nCargo: {cargo}\nSenha: {senha}\nStatus: {status}\nE-mail: {email}")
        #Access.cadastrarUsuario(cpf,senha,cargo,nome,status,email)

    def voltar_pagina(self, root):
        root.destroy()

    def switch(self, switch_var):
        switch_var.set("Inativo")

    def elementos_tela(self, root):
        widgets = {}

        widgets['cpf'] = ctk.CTkEntry(root, width=620, height=35, placeholder_text='CPF')
        widgets['cpf'].grid(row=1,column=0,columnspan=2, padx=10, pady=10)

        widgets['nome'] = ctk.CTkEntry(root, width=620, height=35, placeholder_text='Nome')
        widgets['nome'].grid(row=2,column=0,columnspan=2, padx=10, pady=10)
        
        widgets['e-mail'] = ctk.CTkEntry(root, width=620, height=35, placeholder_text='E-mail')
        widgets['e-mail'].grid(row=3,column=0,columnspan=2, padx=10, pady=10)

        list_cargos = ["Administrador", "Gerente de Produção", "Assistente de Produção"]
        opmenu_var = ctk.StringVar(value='Escolha um Cargo')
        widgets['cargo'] = ctk.CTkOptionMenu(root, width=300, height=35, values=list_cargos, variable=opmenu_var)
        widgets['cargo'].grid(row=4, column=0, padx=10, pady=10)

        switch_var = ctk.StringVar(value="Ativo")
        widgets['status'] = ctk.CTkSwitch(root, textvariable=switch_var, width=300, height=35, variable=switch_var, onvalue="Ativo", offvalue="Inativo")
        widgets['status'].grid(row=4, column=1, padx=10, pady=10)

        btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.voltar_pagina(root))
        btn_cancelar.grid(row=5, column=0, padx=10, pady=10)

        btn_registrar = ctk.CTkButton(root, width=300, height=35, text='Registrar', command=lambda: self.cadastrar_usuario(
            widgets['cpf'].get(),widgets['cargo'].get(), widgets['nome'].get(), widgets['status'].get(),widgets['e-mail'].get()))
        btn_registrar.grid(row=5, column=1, padx=10, pady=10)
