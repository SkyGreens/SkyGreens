from tkinter import *
import customtkinter as ctk

from style import Style
from access import Access

class Relatorio:
    def __init__(self, root, main_instance):
        self.root = root
        self.main = main_instance
        self.choice = None 
        self.choicemenu = None
        
        self.frame = Frame(self.root)
        self.frame.pack(side=LEFT)
        self.frame.configure(background=Style.color('bg'))

        cont_frame = Frame(self.frame, bg=Style.color('bg'))
        cont_frame.pack(fill="x", padx=10, pady=10)

        btn_voltar = ctk.CTkButton(cont_frame, text="", image=Style.img('img_icon_voltar'), font=Style.font_style(), width=20, height=20, corner_radius=10,
                                   command=self.show_telaAnterior, fg_color=Style.color('fg_2'), hover_color=Style.color('hover_2'),
                                   border_width=3, border_color=Style.color('hover_2'))
        btn_voltar.pack(pady=5, padx=5, side=LEFT)

        pesq_label = ctk.CTkLabel(cont_frame, text="Selecione o Conteúdo:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=5, side=LEFT)
        
        def escolhacont(choice):
            self.choice = choice
            if self.choice == "Fornecedores":
                self.choicemenu = Access.listarFornecedores()
                self.mostrar_dados(['ID', 'Nome', 'CNPJ', 'Endereço', 'Status', 'Email', 'Telefone', 'Cidade', 'Estado', 'País', 'Inscrição Estadual', 'Semente'], self.choicemenu)
            elif self.choice == "Produção":
                self.choicemenu = Access.listarProducao()
                self.mostrar_dados(['ID', 'Nome do Produto','Quantidade','Status', 'Tempo de Cultivo', 'Dias restantes','Data Inicio'], self.choicemenu)
            elif self.choice == "Pedidos de Venda":
                self.choicemenu = Access.listarpedidosVenda()
                self.mostrar_dados(['Cliente', 'Quantidade', 'Produto', 'Tempo de Cultivo','Status'], self.choicemenu)
            elif self.choice == "Pedidos de Compras":
                self.choicemenu = Access.listarpedidosCompra()
                self.mostrar_dados(['Fornecedor', 'Quantidade', 'Semente'], self.choicemenu)

        optionmenu_var = ctk.StringVar(value="Escolha o conteúdo")
        list_cont = ["Produção", "Fornecedores", "Pedidos de Venda", "Pedidos de Compras"]
        self.cont = ctk.CTkOptionMenu(cont_frame, width=800, height=35, values=list_cont, variable=optionmenu_var, command=escolhacont, fg_color=Style.color('fg'))
        self.cont.pack(pady=5, padx=5, side=LEFT)
    
        btn_gerarRelatorio = ctk.CTkButton(cont_frame, text='Gerar Relatório', font=('Arial', 15, 'bold'), corner_radius=3, width=150, height=40,
                                        command=lambda: Style.gerar_relatorio(self.choicemenu, self.choice), fg_color=Style.color('fg'), hover_color=Style.color('hover'))
        btn_gerarRelatorio.pack(pady=5, padx=10, side=RIGHT)
        
        self.mostra_frame = Frame(self.frame, bg=Style.color('bg_frame'), width=1100, height=350)
        self.mostra_frame.pack(fill="both", expand=True, pady=10, padx=10)

    def mostrar_dados(self, headers, dados=None):
        
        for widget in self.mostra_frame.winfo_children():
            widget.destroy()

        for col, header in enumerate(headers):
            label = Label(self.mostra_frame, text=header, font=("Arial", 10, 'bold'), bg=Style.color('bg_frame'))
            label.grid(row=0, column=col, padx=5, pady=5)
        if dados != None:
            for row, item in enumerate(dados, start=1):
                for col, value in enumerate(item.values()):
                    label = Label(self.mostra_frame, text=value, font=("Arial", 10), bg=Style.color('bg_frame'))
                    label.grid(row=row, column=col, padx=5, pady=5)

    def show_telaAnterior(self):
        self.main.mostrar_tela("telaProducao")

    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()