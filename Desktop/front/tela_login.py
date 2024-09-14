from tkinter import *
import customtkinter as ctk


'''COLORS
HOVER/PRINCIPAL =  #316133
MENU = #3ab355
background=#dfeedf
'''

fg = "#3ab355"
hover = "#316133"
bg = "#dfeedf"

if __name__ == "__main__":
    
    root = Tk()
    root.title("SkyGreens")
    root.geometry("1300x500")
    root.configure(background=bg)
    
    
    frame = Frame(root)
    frame.pack(side=TOP,anchor=CENTER)
    frame.configure(background=bg)
    
    
    nome = ctk.CTkEntry(frame,placeholder_text="Usuario")
    nome.pack(pady=15,padx=10,side=TOP)
    
    senha = ctk.CTkEntry(frame,placeholder_text="Senha")
    senha.pack(pady=10,padx=10,side=TOP)
    
    button_ok = ctk.CTkButton(frame,text="Ok",font=('Arial',15,'bold'),corner_radius=3,fg_color=fg,hover_color=hover)
    button_ok.pack(pady=50,padx=10,side=LEFT)
        
        

    root.mainloop()