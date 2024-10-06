from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #pip install customtkinter matplotlib
import matplotlib.pyplot as plt

#from cd_fornecedor import cdFornecedor

fg = "#3ab355"  # menu
hover = "#316133"  # hover/principal
bg = "#dfeedf"  # background

class telaHome:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Frame principal configurado para usar pack
        self.frame = Frame(self.root, background=bg)
        self.frame.pack(fill="both", expand=True)  # O frame deve se ajustar ao tamanho da janela

        # Card 1
        card1 = ctk.CTkFrame(self.frame, width=260, height=440, corner_radius=10)
        card1.place(x=45, y=15)

        label_card1 = ctk.CTkLabel(card1, text="Aprenda a Usar o Sistema", font=("Arial", 18))
        label_card1.place(x=20, y=20)

        btn_saibamais1 = ctk.CTkButton(card1, text="Saiba mais", width=200)
        btn_saibamais1.place(x=20, y=150)

        # Card 2
        card2 = ctk.CTkFrame(self.frame, width=260, height=440, corner_radius=10)
        card2.place(x=350, y=15)

        label_card2 = ctk.CTkLabel(card2, text="Pedidos", font=("Arial", 18))
        label_card2.place(x=20, y=20)

        btn_saibamais2 = ctk.CTkButton(card2, text="Saiba mais", width=200)
        btn_saibamais2.place(x=20, y=150)

        # Card 3
        card3 = ctk.CTkFrame(self.frame, width=260, height=440, corner_radius=10)
        card3.place(x=650, y=15)

        label_card3 = ctk.CTkLabel(card3, text="Outros", font=("Arial", 18))
        label_card3.place(x=20, y=20)

        btn_saibamais3 = ctk.CTkButton(card3, text="Saiba mais", width=200)
        btn_saibamais3.place(x=20, y=150)

        # Função para gerar o gráfico circular
        def criar_grafico(valor, desc, titulo):
            fig, ax = plt.subplots()
            fig.patch.set_alpha(0.0)
            ax.pie(valor, labels=desc, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Para manter o formato do gráfico como círculo
            plt.title(titulo)
            plt.title(titulo, fontsize=16, color="black")
            return fig

        # Gráfico de Produção Geral
        prod_valor = [46, 35, 19]
        prod_desc = ['Plantio', 'Adubo', 'Colheita']
        fig1 = criar_grafico(prod_valor, prod_desc, "Produção Geral")
        canvas1 = FigureCanvasTkAgg(fig1, self.frame)
        canvas1.draw()
        canvas1.get_tk_widget().place(x=955, y=15, height=200, width=300)
        canvas1.get_tk_widget().config(bg=bg, highlightthickness=0)

        # Gráfico de Sementes
        se_valor = [100, 46, 35]
        se_nomes = ['Alface', 'Tomate', 'Milho']
        fig2 = criar_grafico(se_valor, se_nomes, "Sementes")
        canvas2 = FigureCanvasTkAgg(fig2, self.frame)
        canvas2.draw()
        canvas2.get_tk_widget().place(x=955, y=250, height=200, width=300)
        canvas2.get_tk_widget().config(bg=bg, highlightthickness=0)

    # Função para exibir a tela
    def mostrar(self):
        self.frame.pack(fill="both", expand=True)

    # Função para esconder a tela
    def esconder(self):
        self.frame.pack_forget()
    
