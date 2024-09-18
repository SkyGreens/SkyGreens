from tkinter import *
import customtkinter as ctk


from access import Access

'''COLORS
HOVER/PRINCIPAL =  #316133
MENU = #3ab355
background=#dfeedf
'''

fg = "#3ab355"
hover = "#316133"
bg = "#dfeedf"

class login:
    def __init__(self, root):
        self.root = root
        Access(root,self)

if __name__ == "__main__":

    def verificar():
        if nome and senha:
            login(root)
    
    root = Tk()
    root.title("SkyGreens")
    root.geometry("1300x500")
    root.configure(background=bg)
    
    
    frame = Frame(root)
    frame.pack(side=TOP,anchor=CENTER)
    frame.configure(background=bg)
    
    nome = ctk.CTkEntry(frame,placeholder_text="Usuario")
    nome.pack(pady=10,padx=1,side=TOP)
    
    senha = ctk.CTkEntry(frame,placeholder_text="Senha")
    senha.pack(pady=10,padx=1,side=TOP)
    
    button_ok = ctk.CTkButton(frame,text="Ok",font=('Arial',15,'bold'),corner_radius=3,fg_color=fg,hover_color=hover, command=lambda: verificar())
    button_ok.pack(pady=10,padx=1,side=TOP)

    root.mainloop()