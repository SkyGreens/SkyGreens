from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter

fg = "#316133"  # Cor para botões
hover = "#5d732f"  # Cor ao passar o mouse
bg = "#D9D9D9"  # Cor de fundo

bg_frame = "#E7E7E7"  # Cor de fundo do frame

class telaPedidos:
    def __init__(self,root,controller):
        self.root = root
        self.controller = controller
        self.frame= Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=bg)


        #escrever aqui















        label = ctk.CTkLabel(self.frame, text="Frame Pedidos",font=('Arial',15,'bold'),corner_radius=3,width=200,height=40,fg_color=hover)
        label.pack(pady=10,padx=1,side=LEFT)

    
    
    
    #nao fuçar
    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()    

