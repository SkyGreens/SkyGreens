from tkinter import * #pip install tkinter
import customtkinter as ctk #pip install customtkinter

from style import Style
from access import Access
from tela_base import telaBase

class telaHome:

    def __init__(self, root, main_instance):
        self.root = root
        self.main = main_instance
        
        self.frame = Frame(self.root, background=Style.color('bg'))
        self.frame.pack(fill="both", expand=True)
        
        # Card 1
        card1 = ctk.CTkFrame(self.frame, width=350, height=440, corner_radius=10)
        card1.place(x=45, y=15)

        self.listaSementes_frame = ctk.CTkScrollableFrame(card1, width=350, height=400)
        self.listaSementes_frame.pack( pady=10, padx=10)

        self.lista_sementes()

        btn_saibamais2 = ctk.CTkButton(card1, text="Insumos", width=392,fg_color=Style.color('fg'),hover_color=Style.color('hover'),command=self.show_sementes)
        btn_saibamais2.place(x=0, y=405)

        # Card 2
        card2 = ctk.CTkFrame(self.frame, width=359, height=440, corner_radius=10)
        card2.place(x=500, y=15)

        self.listaPedidos_frame = ctk.CTkScrollableFrame(card2, width=350, height=400)
        self.listaPedidos_frame.pack(pady=10, padx=10)

        self.lista_pedidos()

        btn_saibamais3 = ctk.CTkButton(card2, text="Pedidos", width=392,fg_color=Style.color('fg'),hover_color=Style.color('hover'),command=self.show_pedidos)
        btn_saibamais3.place(x=0, y=405)

        #graficos
        
        pedidosVenda = Access.listarpedidosVenda()
        pedidosCompra = Access.listarpedidosCompra()
        producao = Access.listarProducao()
        
        qtd_venda = sum(pedido['qtd'] for pedido in pedidosVenda)
        qtd_compra = sum(pedido['qtd'] for pedido in pedidosCompra)
        qtd_producao = sum(producao_item['qtd'] for producao_item in producao)

        prod_valor = [qtd_venda, qtd_compra, qtd_producao]
        prod_desc = ['Pedidos Venda', 'Pedidos Compra', 'Em Produção']
        
        canvas = Style.criar_grafico_circular(self.frame,prod_valor, prod_desc, "Produção Geral")
        canvas.draw()
        canvas.get_tk_widget().place(x=895, y=15, height=240, width=380)
        canvas.get_tk_widget().config(bg=Style.color('bg'), highlightthickness=0)

        
        #===
        
        estoque = Access.listarEstoque()
        
        se_valor = [item['qtd'] for item in estoque]
        se_desc = [item['nome_semente'] for item in estoque]

        quantidade_total = sum(se_valor)
        se_valor = [(valor / quantidade_total) * 100 for valor in se_valor]
        
        canvas = Style.criar_grafico_circular(self.frame,se_valor, se_desc, "Estoque")
        canvas.draw()
        canvas.get_tk_widget().place(x=895, y=250, height=240, width=380)
        canvas.get_tk_widget().config(bg=Style.color('bg'), highlightthickness=0)
    
    def show_sementes(self):
            self.main.mostrar_tela("listaInsumos",9)
    def show_pedidos(self):
            self.main.mostrar_tela("pedidoVenda",11)
    
    def lista_pedidos(self):
        pedidos = Access.listarpedidosVenda()
        
        for i in pedidos:
                
            ped_frame = ctk.CTkFrame(self.listaPedidos_frame, corner_radius=10)
            ped_frame.pack(fill="x", padx=10, pady=5)
            
            ped_label = ctk.CTkLabel(ped_frame, text=f"ID: {i['idvenda']} | {i['cliente']['razaoSocial']} | {i['qtd']}", font=Style.font_style())
            ped_label.pack(pady=5)

        if not pedidos:
            msg_label = ctk.CTkLabel(self.listaPedidos_frame, text="Nenhum usuário encontrado.", font=Style.font_style())
            msg_label.pack(pady=5)

    def lista_sementes(self):
        sementes = Access.listarSementes()
        
        for i in sementes:
                
            sem_frame = ctk.CTkFrame(self.listaSementes_frame, corner_radius=10)
            sem_frame.pack(fill="x", padx=10, pady=5)

            sem_label = ctk.CTkLabel(sem_frame, text=f"{i['nome']}", font=Style.font_style())
            sem_label.pack(pady=5)
                
        if not sementes:
            msg_label = ctk.CTkLabel(self.listaSementes_frame, text="Nenhum Insumo Cadastrado", font=Style.font_style())
            msg_label.pack(pady=5)

    def mostrar(self):
        self.frame.pack(fill="both", expand=True)

    def esconder(self):
        self.frame.pack_forget()
    
