from tkinter import *  # pip install tkinter
import customtkinter as ctk  # pip install customtkinter

# Simulação da tela de cadastro de pedidos
class cdPedido:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Cadastrar Pedido")
        self.root.geometry("400x300")
        self.root.configure(bg="#D9D9D9")

        # Labels e Entradas para cadastrar um novo pedido
        Label(self.root, text="Nome do Pedido:", bg="#D9D9D9", font=("Arial", 14)).pack(pady=10)
        self.nome_entry = Entry(self.root, font=("Arial", 12), width=30)
        self.nome_entry.pack(pady=5)

        Label(self.root, text="Quantidade:", bg="#D9D9D9", font=("Arial", 14)).pack(pady=10)
        self.quantidade_entry = Entry(self.root, font=("Arial", 12), width=30)
        self.quantidade_entry.pack(pady=5)

        Label(self.root, text="Preço:", bg="#D9D9D9", font=("Arial", 14)).pack(pady=10)
        self.preco_entry = Entry(self.root, font=("Arial", 12), width=30)
        self.preco_entry.pack(pady=5)

        # Botão de salvar o pedido
        btn_salvar = ctk.CTkButton(self.root, text='Salvar Pedido', font=('Arial', 15, 'bold'), corner_radius=3, 
                                   width=100, height=40, fg_color="#316133", hover_color="#5d732f", 
                                   command=self.salvar_pedido)
        btn_salvar.pack(pady=20)

    def salvar_pedido(self):
        # Lógica para salvar o pedido pode ser inserida aqui
        print(f"Pedido cadastrado: {self.nome_entry.get()}, {self.quantidade_entry.get()} unidades, R$ {self.preco_entry.get()}")
        self.root.destroy()


class telaPedidos:
    
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background="#D9D9D9")

        # Frame de pesquisa de pedidos
        pesquisar_frame = Frame(self.frame, bg="#D9D9D9")
        pesquisar_frame.pack(fill="x", padx=10, pady=10)

        self.pesq_conteudo = StringVar()
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Pedido:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=1, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=800, height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>", self.pedido_lista)

        # Botão para abrir a tela de cadastrar pedidos
        btn_cadastrarPedido = ctk.CTkButton(pesquisar_frame, text='Cadastrar Pedido', font=('Arial', 15, 'bold'),
                                            corner_radius=3, width=100, height=40, fg_color="#316133", 
                                            hover_color="#5d732f", command=lambda: cdPedido())
        btn_cadastrarPedido.pack(pady=5, padx=10, side=RIGHT)

        # Frame de lista de pedidos
        self.lista_frame = ctk.CTkScrollableFrame(self.frame, width=1100, height=350, fg_color="#E7E7E7")
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Carregar a lista de pedidos
        self.pedido_lista()

    def pedido_lista(self, event=None):
        pedidos = [{"id": "1", "nome": "Pedido A", "quantidade": "10", "preco": "100.00"},
                   {"id": "2", "nome": "Pedido B", "quantidade": "5", "preco": "250.00"},
                   {"id": "3", "nome": "Pedido C", "quantidade": "20", "preco": "150.00"}]

        # Limpar os pedidos anteriores
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        termoPesq = self.pesq_conteudo.get().lower()

        # Exibir pedidos correspondentes à pesquisa
        for i in pedidos:
            if (termoPesq in i['id'].lower() or
                termoPesq in i['nome'].lower() or
                termoPesq in i['quantidade'].lower()):
                
                pedido_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                pedido_frame.pack(fill="x", padx=10, pady=5)

                pedido_label = ctk.CTkLabel(pedido_frame, 
                                            text=f"{i['id']} - {i['nome']} - Quantidade: {i['quantidade']} - Preço: R$ {i['preco']}", 
                                            font=("Arial", 14))
                pedido_label.pack(pady=5)

        if not pedidos:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Nenhum pedido encontrado.", font=("Arial", 14))
            msg_label.pack(pady=5)

    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()
