from tkinter import *
import customtkinter as ctk
from style import Style
from access import Access

class telaMonitoramento:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))
        
        self.filtro_var = StringVar(value="Produção")
        filtro_options = ["Disponivel", "Produção"]
        self.filtro_menu = ctk.CTkOptionMenu(self.frame, variable=self.filtro_var, values=filtro_options,command=self.aplicar_filtro,fg_color=Style.color('fg'))
        self.filtro_menu.pack(pady=2, padx=18, anchor=W)

        self.cards_frame = ctk.CTkScrollableFrame(self.frame, orientation="horizontal", width=1200, height=500, fg_color=Style.color('bg'))
        self.cards_frame.pack(fill="x", expand=True, side=TOP)

        self.dados = Access.listarPrateleira()
        self.prod_desc = ['Total', 'Restante']
        self.exibir_prateleiras("Produção")

    def aplicar_filtro(self, filtro):
        self.exibir_prateleiras(filtro)

    def exibir_prateleiras(self, filtro):
        for widget in self.cards_frame.winfo_children():
            widget.destroy()  # Limpa os cartões anteriores
            
        a = 0
        for i in self.dados:

            if i['disponivel'] != filtro:
                continue

            a += 1
            card = ctk.CTkFrame(self.cards_frame, width=280, height=440, corner_radius=10,
                                fg_color=Style.color('fg_2'), border_width=3, border_color=Style.color('hover_2'))
            card.grid(row=1, column=a, padx=10, pady=10)

            label_prateleira = ctk.CTkLabel(card, text=f"Prateleira {i['id']}", text_color="black", font=Style.font_style())
            label_prateleira.place(x=10, y=10)

            if i["producao"]:
                canvas = Style.criar_grafico_barras_verticais(card, i["producao"]["graf_valor"], self.prod_desc, "Dias de Cultivo")
                canvas.draw()
                canvas.get_tk_widget().place(x=20, y=60, height=200, width=240)
                canvas.get_tk_widget().config(bg=Style.color('fg_2'), highlightthickness=0)

                label_codigo = ctk.CTkLabel(card, text=f"Codigo: {i['producao']['idseed']}", text_color="black", font=Style.font_style())
                label_codigo.place(x=10, y=340)
                
                label_semente = ctk.CTkLabel(card, text=f"{i['producao']['nome_semente']}", text_color="black", font=Style.font_style())
                label_semente.place(x=10, y=370)
            
            if i['disponivel'] == "Disponivel":
                label_imagem = ctk.CTkLabel(card, image=Style.img('img_icon_ok_prat'), text="",width=100, height=100)
                label_imagem.place(relx=0.5, rely=0.5, anchor=CENTER)
            
            label_status = ctk.CTkLabel(card, text=f"Status: {i['disponivel']}", text_color="black", font=Style.font_style())
            label_status.place(x=10, y=400)

    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()
