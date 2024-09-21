from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter

fg = "#3ab355"  # Cor para botões
hover = "#316133"  # Cor ao passar o mouse
bg = "#dfeedf"  # Cor de fundo

class telaFornecedor:

    
    def __init__(self, root, controller):
        #elementos
        self.root = root
        self.controller = controller
        self.frame = Frame(self.root)
        self.frame.pack(side=TOP)
        self.frame.configure(background=bg)

        label = ctk.CTkLabel(self.frame, text="Frame Fornecedor",font=('Arial',15,'bold'),corner_radius=3,width=200,height=40,fg_color=hover)
        label.pack(pady=10,padx=1,side=LEFT)


    #função para abrir a tela clicada
    def mostrar(self):
        self.frame.pack()
        
    #esconder as outras telas
    def esconder(self):
        self.frame.pack_forget()