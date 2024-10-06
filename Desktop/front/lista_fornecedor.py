import customtkinter as ctk # pip install customtkinter
from tkinter import Toplevel # pip install tkinter
from tkinter import *

fg = "#3ab355"  # menu
hover = "#316133"  # hover/principal
bg = "#dfeedf"  # background

class todosFornecedores():
    
    def __init__(self,callback,roota):

        jn_x = 640
        jn_y = 560
        self.roota = roota
        self.root = Toplevel()
        self.callback = callback
        self.root.title("Cadastrar Fornecedor")
        self.root.geometry(f"{jn_x}x{jn_y}")
        self.root.overrideredirect(True)
        self.root.configure(background='#dfeedf')
        
        self.centralizar_janela(self.root, jn_x, jn_y)
        self.elementos_tela(self.root)
        self.root.maxsize(jn_x, jn_y)
        self.root.minsize(jn_x, jn_y)
        self.root.mainloop()
    
    
    def voltar_janela(self,jn):
        jn.destroy()
        self.callback.fornecedor_lista()
        
    def centralizar_janela(self,root, largura, altura):

        tela_largura = root.winfo_screenwidth()
        tela_altura = root.winfo_screenheight()

        x = (tela_largura // 2) - (largura // 2)
        y = (tela_altura // 2) - (altura // 2)

        root.geometry(f"{largura}x{altura}+{x}+{y}")
    
    def elementos_tela(self,root):
        
        frame = Frame(root)
        frame.pack(side=TOP)
        frame.configure(background=bg)

        pesquisar_frame = Frame(frame, bg=bg)
        pesquisar_frame.pack(fill="x", padx=10, pady=10)
        
        self.lista_frame = ctk.CTkScrollableFrame(frame, width=600, height=400)
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)
        
        btn_ok = ctk.CTkButton(pesquisar_frame, text='Ok', font=('Arial', 15, 'bold'), corner_radius=3, width=80, height=30,
                            fg_color=fg, hover_color=hover,command=lambda:self.voltar_janela(root))
        btn_ok.pack(pady=5, padx=10, side=RIGHT)
        
        self.callback.fornecedor_lista(1)