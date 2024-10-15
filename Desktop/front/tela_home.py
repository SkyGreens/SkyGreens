from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #pip install customtkinter matplotlib
import matplotlib.pyplot as plt

#from cd_fornecedor import cdFornecedor

fg = "#316133"  # Cor para botões
hover = "#5d732f"  # Cor ao passar o mouse
bg = "#D9D9D9"  # Cor de fundo

bg_frame = "#E7E7E7"  # Cor de fundo do frame

class telaHome:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Frame principal configurado para usar pack
        self.frame = Frame(self.root, background=bg)
        self.frame.pack(fill="both", expand=True)

        # Card 1
        card1 = ctk.CTkFrame(self.frame, width=260, height=440, corner_radius=10)
        card1.place(x=45, y=15)

        self.listaFornecedores_frame = ctk.CTkScrollableFrame(card1, width=200, height=400)
        self.listaFornecedores_frame.pack( pady=10, padx=10)

        self.lista_fornecedores()

        btn_saibamais1 = ctk.CTkButton(card1, text="Fornecedores", width=242,fg_color=fg,hover_color=hover)
        btn_saibamais1.place(x=0, y=405)

        # Card 2
        card2 = ctk.CTkFrame(self.frame, width=260, height=440, corner_radius=10)
        card2.place(x=350, y=15)

        self.listaSementes_frame = ctk.CTkScrollableFrame(card2, width=200, height=400)
        self.listaSementes_frame.pack( pady=10, padx=10)

        self.lista_sementes()

        btn_saibamais2 = ctk.CTkButton(card2, text="Sementes", width=242,fg_color=fg,hover_color=hover)
        btn_saibamais2.place(x=0, y=405)

        # Card 3
        card3 = ctk.CTkFrame(self.frame, width=260, height=440, corner_radius=10)
        card3.place(x=650, y=15)

        self.listaPedidos_frame = ctk.CTkScrollableFrame(card3, width=200, height=400)
        self.listaPedidos_frame.pack(pady=10, padx=10)

        self.lista_pedidos()

        btn_saibamais3 = ctk.CTkButton(card3, text="Pedidos", width=242,fg_color=fg,hover_color=hover)
        btn_saibamais3.place(x=0, y=405)

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
        prod_desc = ['Plantio', 'Pedidos', 'Colheita']
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

    def lista_pedidos(self):
        pedidos = [{"id":"000021","nome":"Alface","qtd":10},
                   {"id":"000315","nome":"Tomate","qtd":2},
                   {"id":"000561","nome":"Milho","qtd":25},
                   {"id":"000369","nome":"Pocã","qtd":20},
                   {"id":"000456","nome":"Banana","qtd":30},
                   {"id":"000159","nome":"Maça","qtd":15}]
        
        for i in pedidos:
                
            ped_frame = ctk.CTkFrame(self.listaPedidos_frame, corner_radius=10)
            ped_frame.pack(fill="x", padx=10, pady=5)

            ped_label = ctk.CTkLabel(ped_frame, text=f"{i['id']} | {i['nome']} | {i['qtd']}", font=("Arial", 14))
            ped_label.pack(pady=5)
                
        if not pedidos:
            msg_label = ctk.CTkLabel(self.listaPedidos_frame, text="Nenhum usuário encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)

    def lista_fornecedores(self):
        fornecedores = [{"id":"1","nome":"Carlos Alberto"},
                     {"id":"2","nome":"Carlos Alberto"},
                     {"id":"3","nome":"Carlos Alberto"},
                     {"id":"4","nome":"Carlos Alberto"},
                     {"id":"5","nome":"Carlos Alberto"},
                     {"id":"6","nome":"Carlos Alberto"},
                     {"id":"7","nome":"Carlos Alberto"},
                     {"id":"8","nome":"Carlos Alberto"},
                     {"id":"9","nome":"Carlos Alberto"}]
        for i in fornecedores:
                
            for_frame = ctk.CTkFrame(self.listaFornecedores_frame, corner_radius=10)
            for_frame.pack(fill="x", padx=5, pady=5)

            lb_for = ctk.CTkLabel(for_frame, text=f"{i['id']} - {i['nome']}", font=("Arial", 14))
            lb_for.pack(pady=5)
                
        if not fornecedores:
            msg_label = ctk.CTkLabel(self.listaFornecedores_frame, text="Nenhum usuário encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)

    def lista_sementes(self):
        sementes = [{"nome":"Alface"},
                     {"nome":"Tomate"},
                     {"nome":"Milho"},
                     {"nome":"Azeitona"},
                     {"nome":"Mamao"},
                     {"nome":"Pocã"}]
        
        for i in sementes:
                
            sem_frame = ctk.CTkFrame(self.listaSementes_frame, corner_radius=10)
            sem_frame.pack(fill="x", padx=10, pady=5)

            sem_label = ctk.CTkLabel(sem_frame, text=f"{i['nome']}", font=("Arial", 14))
            sem_label.pack(pady=5)
                
        if not sementes:
            msg_label = ctk.CTkLabel(self.listaSementes_frame, text="Nenhum usuário encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)

    # Função para exibir a tela
    def mostrar(self):
        self.frame.pack(fill="both", expand=True)

    # Função para esconder a tela
    def esconder(self):
        self.frame.pack_forget()
    
