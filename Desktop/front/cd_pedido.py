from tkinter import *  # pip install tkinter
import customtkinter as ctk  # pip install customtkinter



class cadastrarPedido:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Cadastrar Pedido")
        self.root.geometry("400x300")
        self.root.configure(bg="#D9D9D9")

        
        Label(self.root, text="Nome do Pedido:", bg="#D9D9D9", font=("Arial", 14)).pack(pady=10)
        self.nome_entry = Entry(self.root, font=("Arial", 12), width=30)
        self.nome_entry.pack(pady=5)

        Label(self.root, text="Quantidade:", bg="#D9D9D9", font=("Arial", 14)).pack(pady=10)
        self.quantidade_entry = Entry(self.root, font=("Arial", 12), width=30)
        self.quantidade_entry.pack(pady=5)

        Label(self.root, text="Preço:", bg="#D9D9D9", font=("Arial", 14)).pack(pady=10)
        self.preco_entry = Entry(self.root, font=("Arial", 12), width=30)
        self.preco_entry.pack(pady=5)

        
        btn_salvar = ctk.CTkButton(self.root, text='Salvar Pedido', font=('Arial', 15, 'bold'), corner_radius=3, 
                                   width=100, height=40, fg_color="#316133", hover_color="#5d732f", 
                                   command=self.salvar_pedido)
        btn_salvar.pack(pady=20)

    def salvar_pedido(self):
        
        print(f"Pedido cadastrado: {self.nome_entry.get()}, {self.quantidade_entry.get()} unidades, R$ {self.preco_entry.get()}")
        self.root.destroy()