import customtkinter as ctk # pip install customtkinter
from tkinter import Toplevel # pip install tkinter

from style import Style
from access import Access

class perfilUser:
    def __init__(self):
        jn_x = 500
        jn_y = 650
        
        root = Toplevel()
        root.title("Perfil do Usuário")
        root.geometry(f"{jn_x}x{jn_y}")
        root.wm_attributes('-toolwindow', 1)
        
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

        result = Access.visualizarPerfil()
        for i in result:
            email = i['email']
            status =  i['ativo']
            cargo = i['cargo']
            nome =  i['nome']
            cpf = i['cpf']
        
        def voltar_pagina():
            root.destroy()

        main_frame = ctk.CTkFrame(root)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        prof_img = ctk.CTkLabel(main_frame, text="👤", width=100, height=100, font=("Arial", 40))
        prof_img.pack(pady=(20, 10))

        lb_nome = ctk.CTkLabel(main_frame, text=f"{nome}", font=("Arial", 20, "bold"))
        lb_nome.pack()
        lb_cargo = ctk.CTkLabel(main_frame, text=f"{cargo}", font=Style.font_style())
        lb_cargo.pack()

        frame_nomecompleto = ctk.CTkFrame(main_frame)
        frame_nomecompleto.pack(pady=(40, 10), padx=10, fill="x")
        lb_nomecompleto = ctk.CTkLabel(frame_nomecompleto, text=f"Nome Completo: {nome}", corner_radius=8, height=30)
        lb_nomecompleto.pack(pady=5, padx=10)

        frame_email = ctk.CTkFrame(main_frame)
        frame_email.pack(pady=(0, 10), padx=10, fill="x")
        lb_email = ctk.CTkLabel(frame_email, text=f"E-mail: {email}", corner_radius=8, height=30)
        lb_email.pack(pady=5, padx=10)

        frame_senha = ctk.CTkFrame(main_frame)
        frame_senha.pack(pady=(0, 10), padx=10, fill="x")
        lb_senha = ctk.CTkLabel(frame_senha, text=f"CPF: {cpf}", corner_radius=8, height=30)
        lb_senha.pack(pady=5, padx=10)

        frame_status = ctk.CTkFrame(main_frame)
        frame_status.pack(pady=(0, 10), padx=10, fill="x")
        status1 = "Inativo" if status == False else "Ativo"
        lb_status = ctk.CTkLabel(frame_status, text=f"Status: {status1}", corner_radius=8, height=30)
        lb_status.pack(pady=5, padx=10)

        frame_emp = ctk.CTkFrame(main_frame)
        frame_emp.pack(pady=(0, 10), padx=10, fill="x")
        lb_emp = ctk.CTkLabel(frame_emp, text="Empresa: SkyGreens", corner_radius=8, height=30)
        lb_emp.pack(pady=5, padx=10)

        btn_frame = ctk.CTkFrame(main_frame)
        btn_frame.pack(fill="x", pady=(70, 0))
        
        btn_ok = ctk.CTkButton(btn_frame, text="Ok", width=180,fg_color=Style.color('fg'),hover_color=Style.color('hover'),command=voltar_pagina)
        btn_ok.grid( padx=140, pady=20)
    