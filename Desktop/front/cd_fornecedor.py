from tkinter import *  # pip install tkinter
import customtkinter as ctk # pip install customtkinter
from tkinter import messagebox # pip install tkinter

from access import Access

fg = "#3ab355"  # menu
hover = "#316133"  # hover/principal
bg = "#dfeedf"  # background

class cdFornecedor:
    def __init__(self):
        #tem que centralizar na tela
        root = Tk()
        root.title("Cadastrar Fornecedor")
        root.geometry("800x500")
        #root.overrideredirect(True) #remover decorações da janela
        root.configure(background='#dfeedf')
        
        frame_top = Frame(root)
        frame_top.pack(side=TOP,fill="x",anchor = CENTER)
        frame_top.configure(background=hover)

        label = ctk.CTkLabel(frame_top, text="Cadastrar Fornecedor",font=('Arial',15,'bold'))
        label.pack()
        
        btn_voltar = ctk.CTkButton(frame_top, text="<-",font=('Arial',15,'bold'),corner_radius=3,
                                    width=30,height=30,fg_color=fg,hover_color=hover,command=lambda:voltar_pagina())
        btn_voltar.pack(pady=1,padx=3,side=LEFT)


        en_rzsocial = ctk.CTkEntry(root,width=300, height=35,placeholder_text='Razão Social')
        en_rzsocial.pack(side=TOP)
        en_cnpj = ctk.CTkEntry(root,width=300, height=35,placeholder_text='CNPJ')
        en_cnpj.pack(side=TOP)
        en_iscestadual = ctk.CTkEntry(root,width=300, height=35,placeholder_text='Inscrição Estadual')
        en_iscestadual.pack(side=TOP)
        en_email = ctk.CTkEntry(root,width=300, height=35,placeholder_text='Email')
        en_email.pack(side=TOP)
        en_status = ctk.CTkEntry(root,width=300, height=35,placeholder_text='Status')
        en_status.pack(side=TOP)
        en_tell = ctk.CTkEntry(root,width=300, height=35,placeholder_text='Telefone')
        en_tell.pack(side=TOP)
        en_end = ctk.CTkEntry(root,width=300, height=35,placeholder_text='Endereço')
        en_end.pack(side=TOP)
        en_cid = ctk.CTkEntry(root,width=300, height=35,placeholder_text='Cidade')
        en_cid.pack(side=TOP)
        en_est = ctk.CTkEntry(root,width=300, height=35,placeholder_text='Estado')
        en_est.pack(side=TOP)
        en_pais = ctk.CTkEntry(root,width=300, height=35,placeholder_text='País')
        en_pais.pack(side=TOP)

        button_home = ctk.CTkButton(root, text="Cadastrar",font=('Arial',15,'bold'),corner_radius=3,
                                    fg_color=fg,hover_color=hover, command=lambda:cadastrar_fornecedor(en_rzsocial.get()))
        button_home.pack(side=TOP)

        def voltar_pagina():
            messagebox.askokcancel(title='Confirmação', message='Pode ter informações não salvas')  
            root.destroy()
            
        def cadastrar_fornecedor(en_rzsocial):
            print('Fornecedor Cadastrado')
            
            en_cnpj.get()
            en_iscestadual.get(),en_email.get()
            en_status.get(),en_tell.get()
            en_end.get(),en_cid.get()
            en_est.get(),en_pais.get()
            print(en_rzsocial)
            
            #access = Access.cadatroFornecedor(en_status,en_email,en_tell,en_end,
                                              #en_cid,en_est,en_pais,en_iscestadual,en_rzsocial,en_cnpj) 
            

        root.mainloop()


        

    

