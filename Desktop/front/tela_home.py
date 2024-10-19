from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter

from style import Style
from access import Access

class telaHome:

    def __init__(self, root, main_instance):
        self.root = root
        self.main = main_instance
        
        self.frame = Frame(self.root, background=Style.color('bg'))
        self.frame.pack(fill="both", expand=True)

        # Card 1
        card1 = ctk.CTkFrame(self.frame, width=260, height=440, corner_radius=10)
        card1.place(x=45, y=15)

        self.listaFornecedores_frame = ctk.CTkScrollableFrame(card1, width=200, height=400)
        self.listaFornecedores_frame.pack( pady=10, padx=10)

        self.lista_fornecedores()

        btn_saibamais1 = ctk.CTkButton(card1, text="Fornecedores", width=242, fg_color=Style.color('fg'), hover_color=Style.color('hover'), command=self.show_fornecedores)
        btn_saibamais1.place(x=0, y=405)
        # Card 2
        card2 = ctk.CTkFrame(self.frame, width=260, height=440, corner_radius=10)
        card2.place(x=350, y=15)

        self.listaSementes_frame = ctk.CTkScrollableFrame(card2, width=200, height=400)
        self.listaSementes_frame.pack( pady=10, padx=10)

        self.lista_sementes()

        btn_saibamais2 = ctk.CTkButton(card2, text="Sementes", width=242,fg_color=Style.color('fg'),hover_color=Style.color('hover'))
        btn_saibamais2.place(x=0, y=405)

        # Card 3
        card3 = ctk.CTkFrame(self.frame, width=260, height=440, corner_radius=10)
        card3.place(x=650, y=15)

        self.listaPedidos_frame = ctk.CTkScrollableFrame(card3, width=200, height=400)
        self.listaPedidos_frame.pack(pady=10, padx=10)

        self.lista_pedidos()

        btn_saibamais3 = ctk.CTkButton(card3, text="Pedidos", width=242,fg_color=Style.color('fg'),hover_color=Style.color('hover'))
        btn_saibamais3.place(x=0, y=405)

        # Gráfico de Produção Geral
        prod_valor = [46, 35, 19]
        prod_desc = ['Plantio', 'Pedidos', 'Colheita']
        
        canvas = Style.criar_grafico_circular(self.frame,prod_valor, prod_desc, "Produção Geral")
        canvas.draw()
        canvas.get_tk_widget().place(x=955, y=15, height=200, width=300)
        canvas.get_tk_widget().config(bg=Style.color('bg'), highlightthickness=0)

        # Gráfico de Sementes
        se_valor = [100, 46, 35]
        se_desc = ['Alface', 'Tomate', 'Milho']
        
        canvas = Style.criar_grafico_circular(self.frame,se_valor, se_desc, "Sementes")
        canvas.draw()
        canvas.get_tk_widget().place(x=955, y=250, height=200, width=300)
        canvas.get_tk_widget().config(bg=Style.color('bg'), highlightthickness=0)
    
    def show_fornecedores(self):
            from tela_base import telaBase
            self.main.mostrar_tela("telaFornecedor")
    
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

            ped_label = ctk.CTkLabel(ped_frame, text=f"{i['id']} | {i['nome']} | {i['qtd']}", font=Style.font_style())
            ped_label.pack(pady=5)
                
        if not pedidos:
            msg_label = ctk.CTkLabel(self.listaPedidos_frame, text="Nenhum usuário encontrado.", font=Style.font_style())
            msg_label.pack(pady=5)

    def lista_fornecedores(self):
        fornecedores = Access.listarFornecedores()
        for i in fornecedores:
                
            for_frame = ctk.CTkFrame(self.listaFornecedores_frame, corner_radius=10)
            for_frame.pack(fill="x", padx=5, pady=5)

            lb_for = ctk.CTkLabel(for_frame, text=f"{i['id']} - {i['nome']}", font=Style.font_style())
            lb_for.pack(pady=5)
                
        if not fornecedores:
            msg_label = ctk.CTkLabel(self.listaFornecedores_frame, text="Nenhum usuário encontrado.", font=Style.font_style())
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

            sem_label = ctk.CTkLabel(sem_frame, text=f"{i['nome']}", font=Style.font_style())
            sem_label.pack(pady=5)
                
        if not sementes:
            msg_label = ctk.CTkLabel(self.listaSementes_frame, text="Nenhum usuário encontrado.", font=Style.font_style())
            msg_label.pack(pady=5)

    # Função para exibir a tela
    def mostrar(self):
        self.frame.pack(fill="both", expand=True)

    # Função para esconder a tela
    def esconder(self):
        self.frame.pack_forget()
    
