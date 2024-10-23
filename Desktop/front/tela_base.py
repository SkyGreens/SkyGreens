from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter
import os
import sys

from style import Style,MessageBox
from perfil_user import perfilUser


class telaBase:
    
    def __init__(self, root):
        self.root = root
        self.top()
        self.menu()
        self.verificar(1)

    def fechar_programa(self):
        message_box = MessageBox()
        result = message_box.askquestion("Logout", "Deseja voltar a tela de login?")
        if result == 'yes':
            self.root.quit()
            os.execv(sys.executable, ['python'] + sys.argv)
        
    def top(self):
        
        frame_top = Frame(self.root)
        frame_top.pack(side=TOP, fill="x")

        label = ctk.CTkLabel(frame_top, text="SkyGreens", font=('Arial', 20, 'bold'), width=200, height=40, text_color="#353847")
        label.pack(pady=10, side=LEFT)
        
        btn_sair = ctk.CTkButton(frame_top,text="",image=Style.img('img_icon_saida'),width=0,hover_color=Style.color('hover_red'),fg_color=Style.color('fg_red'),command=self.fechar_programa)
        btn_sair.pack(pady=10,padx=10,side=RIGHT)

        btn_perfil = ctk.CTkButton(frame_top,text="",image=Style.img('img_icon_perfil'),width=0,hover_color=Style.color('hover'),fg_color=Style.color('fg'),command=perfilUser)
        btn_perfil.pack(pady=10,padx=5,side=RIGHT)

    def menu(self):
        frame = Frame(self.root)
        frame.pack(side=TOP, anchor=CENTER)
        frame.configure(background=Style.color('bg'))

        buttons = [
            ("Home", lambda: self.verificar(1)),
            ("Monitoramento", lambda: self.verificar(2)),
            ("Fornecedores", lambda: self.verificar(3)),
            ("Produção", lambda: self.verificar(4)),
            ("Pedidos", lambda: self.verificar(5)),
            ("Usuários", lambda: self.verificar(6)),
        ]

        self.menu_buttons = []
        for text, command in buttons:
            button = ctk.CTkButton(frame, text=text, font=('Arial', 15, 'bold'), corner_radius=3, width=200, height=40,
                                   fg_color=Style.color('fg'), hover_color=Style.color('hover'), command=command)
            button.pack(pady=10, padx=1, side=LEFT)
            self.menu_buttons.append(button)

    def verificar(self, n):
        
        for button in self.menu_buttons:
            button.configure(fg_color=Style.color('fg'))

        self.menu_buttons[n-1].configure(fg_color=Style.color('hover'))
        
        telas = ["telaHome", "telaMonitoramento", "telaFornecedor", "telaProducao", "telaPedidos", "telaUsuarios"]
        self.mostrar_tela(telas[n-1])

    def mostrar_tela(self, tela_nome):
        pass
