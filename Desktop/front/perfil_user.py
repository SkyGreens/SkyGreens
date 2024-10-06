import customtkinter as ctk # pip install customtkinter
from tkinter import Toplevel # pip install tkinter

#from access import Access

fg = "#3ab355"  # menu
hover = "#316133"  # hover/principal
bg = "#dfeedf"  # background

class perfilUser:
    def __init__(self,nome,cpf,cargo,status,email):
        jn_x = 640
        jn_y = 300
        self.nome=nome
        self.cpf=cpf
        self.cargo=cargo
        self.status=status
        self.email = email

        root = Toplevel()
        root.title("Perfil")
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
    
    

    def elementos_tela(self, root):

        def voltar_pagina():
            root.destroy()

        lb_nome = ctk.CTkLabel(root, text=f"Nome: {self.nome}",font=('Arial',20,'bold'),width=620,height=35,text_color="#353847")
        lb_nome.grid(row=1, column=0, columnspan=2,padx=10, pady=10)

        lb_cpf = ctk.CTkLabel(root, text=f"CPF: {self.cpf}",font=('Arial',20,'bold'),width=300,height=35,text_color="#353847")
        lb_cpf.grid(row=2, column=0,padx=10, pady=10)
        lb_cargo = ctk.CTkLabel(root, text=f"Cargo: {self.cargo}",font=('Arial',20,'bold'),width=300,height=35,text_color="#353847")
        lb_cargo.grid(row=2, column=1,padx=10, pady=10)
        

        lb_email = ctk.CTkLabel(root, text=f"Email: {self.email}",font=('Arial',20,'bold'),width=620,height=35,text_color="#353847")
        lb_email.grid(row=3, column=0, columnspan=2,padx=10, pady=10)

        lb_empresa = ctk.CTkLabel(root, text="Empresa: SkyGreens",font=('Arial',20,'bold'),width=300,height=35,text_color="#353847")
        lb_empresa.grid(row=4, column=0,padx=10, pady=10)
        lb_status = ctk.CTkLabel(root, text=f"Status: {self.status}",font=('Arial',20,'bold'),width=300,height=35,text_color="#353847")
        lb_status.grid(row=4, column=1,padx=10, pady=10)

        btn_ok = ctk.CTkButton(root, width=620, height=35, text='Ok',command=voltar_pagina)
        btn_ok.grid(row=5, column=0,columnspan = 2, padx=10, pady=10)
    