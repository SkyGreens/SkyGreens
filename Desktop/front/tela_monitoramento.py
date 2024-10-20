from tkinter import *
import customtkinter as ctk

from style import Style

class telaMonitoramento:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))

        cards_frame = ctk.CTkScrollableFrame(self.frame,orientation="horizontal", width=1200, height=500,fg_color=Style.color('bg'))
        cards_frame.pack(fill="x", expand=True, side=TOP)

        #card
        codigo = "5501"
        prateleira = "1"
        semente = "Espinafre"
        status = "Produção"
        prod_valor = [29, 1]  # 29 de 30 dias
        prod_desc = ['Dias', 'Restante']

        for i in range(0,5):

            card = f"card{i}"
            card = ctk.CTkFrame(cards_frame, width=280, height=440, corner_radius=10,fg_color=Style.color('fg_2'),border_width=3,border_color=Style.color('hover_2'))
            card.grid(row=1, column=i, padx=10, pady=10)

            label_prateleira = ctk.CTkLabel(card, text=f"Prateleira {prateleira}",text_color="black", font=Style.font_style())
            label_prateleira.place(x=10, y=10)

            #gráfico
            canvas = Style.criar_grafico_circular(card,prod_valor, prod_desc, "")
            canvas.draw()
            canvas.get_tk_widget().place(x=20, y=60, height=200, width=240)
            canvas.get_tk_widget().config(bg=Style.color('fg_2'), highlightthickness=0)

            label_codigo = ctk.CTkLabel(card, text=f"{codigo}",text_color="black", font=Style.font_style())
            label_codigo.place(x=10, y=340)
            
            label_semente = ctk.CTkLabel(card, text=f"{semente}",text_color="black", font=Style.font_style())
            label_semente.place(x=10, y=370)
            
            label_status = ctk.CTkLabel(card, text=f"Status: {status}...",text_color="black", font=Style.font_style())
            label_status.place(x=10, y=400)


    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()