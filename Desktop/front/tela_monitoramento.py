from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter

fg = "#316133"  # Cor para botões
hover = "#5d732f"  # Cor ao passar o mouse
bg = "#D9D9D9"  # Cor de fundo

class telaMonitoramento:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack(side=TOP)
        self.frame.configure(background=bg)

        label = ctk.CTkLabel(self.frame, text="Frame Monitoramento",font=('Arial',15,'bold'),corner_radius=3,width=200,height=40,fg_color=hover)
        label.pack(pady=10,padx=1,side=LEFT)


    def mostrar(self):
        self.frame.pack() # Exibe a tela

    def esconder(self):
        self.frame.pack_forget()