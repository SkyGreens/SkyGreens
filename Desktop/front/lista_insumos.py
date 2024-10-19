from tkinter import * # pip install tkinter
import customtkinter as ctk # pip install customtkinter

from style import Style
from cd_insumos import cdInsumos


class listaInsumos:

    def __init__(self):
        jn_x = 600
        jn_y = 550

        root = Toplevel()
        root.title("Insumos")
        root.geometry(f"{jn_x}x{jn_y}")
        root.wm_attributes('-toolwindow', 1)
        root.configure(background=Style.color('bg'))

        self.centralizar_janela(root, jn_x, jn_y)
        self.elementos_tela(root)
        root.maxsize(jn_x, jn_y)
        root.minsize(jn_x, jn_y)
        root.mainloop()

    def centralizar_janela(self,root, largura, altura):

        tela_largura = root.winfo_screenwidth()
        tela_altura = root.winfo_screenheight()

        x = (tela_largura // 2) - (largura // 2)
        y = (tela_altura // 2) - (altura // 2)

        root.geometry(f"{largura}x{altura}+{x}+{y}")

    def elementos_tela(self,root):


        pesquisar_frame = Frame(root, bg=Style.color('bg'))
        pesquisar_frame.pack(fill="x", padx=10, pady=10)

        self.pesq_conteudo = StringVar()
        pesq_label = ctk.CTkLabel(pesquisar_frame, text="Pesquisar Insumo:", font=("Arial", 14))
        pesq_label.pack(pady=5, padx=1, side=LEFT)

        self.pesq_entry = ctk.CTkEntry(pesquisar_frame, textvariable=self.pesq_conteudo, width=300,height=35)
        self.pesq_entry.pack(pady=5, padx=10, side=LEFT)
        self.pesq_entry.bind("<KeyRelease>", self.insumos_lista)

        btn_cadastrarInsumo = ctk.CTkButton(pesquisar_frame, text='Cadastrar', font=('Arial', 15, 'bold'), corner_radius=3, width=100, height=40,
                                fg_color=Style.color('fg'), hover_color=Style.color('hover'), command=cdInsumos)
        btn_cadastrarInsumo.pack(pady=5, padx=10, side=RIGHT)

        self.lista_frame = ctk.CTkScrollableFrame(root, width=1100, height=350,fg_color=Style.color('bg_frame'))
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Carrega a lista completa
        self.insumos_lista()

    def insumos_lista(self, event=None):

        insumos = [{"id":"1","nome":"Alface","qtd":"20","fornecedor":"SkyGreens"},
                    {"id":"2","nome":"Tomate","qtd":"20","fornecedor":"SkyGreens"},
                    {"id":"3","nome":"Milho","qtd":"150","fornecedor":"SkyGreens"},
                    {"id":"4","nome":"Banana","qtd":"25","fornecedor":"SkyGreens"},
                    {"id":"5","nome":"Azeitona","qtd":"10","fornecedor":"SkyGreens"},
                    
                    ]

        # Limpar os fornecedores anteriores
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        termoPesq = self.pesq_conteudo.get().lower()

        # Exibir fornecedores correspondentes à pesquisa
        for i in insumos:
            if (termoPesq in i['id'].lower() or
                termoPesq in i['nome'].lower() or
                termoPesq in i['fornecedor'].lower()):
                
                insumo_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
                insumo_frame.pack(fill="x", padx=10, pady=5)

                insumo_label = ctk.CTkLabel(insumo_frame, text=f"{i['id']} | {i['nome']} | {i['qtd']} | {i['fornecedor']}", font=("Arial", 14))
                insumo_label.pack(pady=5)
            
        if not insumos:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Nenhum insumo cadastrado.", font=("Arial", 14))
            msg_label.pack(pady=5)