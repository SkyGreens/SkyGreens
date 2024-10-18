from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter

from perfil_user import perfilUser
from style import Style

fg = "#316133"  # Cor para botões
hover = "#5d732f"  # Cor ao passar o mouse
bg = "#D9D9D9"  # Cor de fundo

#c30000 - vermelho botao
#6f0000 - vermelho hover

class telaBase:
    def __init__(self, root):
        self.root = root
        self.top()
        self.menu()
        self.verificar(1)

    def fechar_programa(self):
        self.root.quit()

    def top(self):
        frame_top = Frame(self.root)
        frame_top.pack(side=TOP, fill="x")

        label = ctk.CTkLabel(frame_top, text="SkyGreens", font=('Arial', 20, 'bold'), width=200, height=40, text_color="#353847")
        label.pack(pady=10, side=LEFT)
        
        btn_sair = ctk.CTkButton(frame_top,text="",image=Style.img('img_icon_saida'),width=0,hover_color="#6f0000",fg_color="#c30000",command=self.fechar_programa)
        btn_sair.pack(pady=10,padx=20,side=RIGHT)

        btn_perfil = ctk.CTkButton(frame_top,text="",image=Style.img('img_icon_perfil'),width=0,hover_color=hover,fg_color="#172200",command=perfilUser)
        btn_perfil.pack(pady=10,padx=20,side=RIGHT)

    def menu(self):
        frame = Frame(self.root)
        frame.pack(side=TOP, anchor=CENTER)
        frame.configure(background=bg)

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
                                   fg_color=fg, hover_color=hover, command=command)
            button.pack(pady=10, padx=1, side=LEFT)
            self.menu_buttons.append(button)

    def verificar(self, n):
        
        for button in self.menu_buttons:
            button.configure(fg_color=fg)

        self.menu_buttons[n-1].configure(fg_color=hover)
        telas = ["telaHome", "telaMonitoramento", "telaFornecedor", "telaProducao", "telaPedidos", "telaUsuarios"]
        self.mostrar_tela(telas[n-1])

    def mostrar_tela(self, tela_nome):
        pass
