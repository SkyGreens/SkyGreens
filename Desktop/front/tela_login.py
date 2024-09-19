from tkinter import *
import customtkinter as ctk

from access import Access


fg = "#3ab355" # menu
hover = "#316133" # hover/principal
bg = "#dfeedf" #background


if __name__ == "__main__":

    #função para pegar o conteudo dos entry e passar como parametro para a função login da classe access
    def chamar(enome,esenha):
        user = enome.get()
        senha = esenha.get()
        Access.login(user,senha)
        
    root = Tk()
    root.title("SkyGreens")
    root.geometry("500x300")
    root.configure(background=bg)
    
    frame = Frame(root)
    frame.pack(side=TOP,anchor=CENTER)
    frame.configure(background=bg)
    
    en_nome = ctk.CTkEntry(frame,placeholder_text="Usuario")
    en_nome.pack(pady=10,padx=1,side=TOP)
    
    en_senha = ctk.CTkEntry(frame,placeholder_text="Senha",show = "*")
    en_senha.pack(pady=10,padx=1,side=TOP)
    
    button_ok = ctk.CTkButton(frame,text="Ok",font=('Arial',15,'bold'),corner_radius=3,fg_color=fg,hover_color=hover
                              , command=lambda: chamar(en_nome,en_senha))
    button_ok.pack(pady=10,padx=1,side=TOP)

    root.mainloop()