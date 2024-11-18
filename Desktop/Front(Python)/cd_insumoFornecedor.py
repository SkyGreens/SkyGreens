from tkinter import *
import customtkinter as ctk  # pip install customtkinter

from style import Style,MessageBox
from access import Access

class cdInsumofornecedor:
    
    def __init__(self, dados=None):
        self.msg_box = MessageBox()
        self.jn_x = 445
        self.jn_y = 600
        
        titulo = "Sementes"
        self.dados = dados
        
        self.root = Style.criar_janela_flutuante(titulo, self.jn_x, self.jn_y)
        self.root.configure(bg=Style.color('bg'))
        self.elementos_tela(self.root)
    
        self.root.mainloop()
        
    def opcaomenu(self, choice, opmenu_var):
        if choice is None:
            opmenu_var.set('Selecione a Semente')
        self.semente_selecionada_id = choice

    def voltar_pagina(self, root):
        root.destroy()

    def elementos_tela(self, root):

        top_frame = Frame(root, bg=Style.color('bg'))
        top_frame.pack(fill="x", padx=10, pady=10)

        label = ctk.CTkLabel(top_frame, text="Sementes Fornecedor", font=('Arial', 25, 'bold'), corner_radius=3, width=200, height=40)
        label.pack(pady=10, padx=1, side=BOTTOM)

        self.lista_frame = ctk.CTkScrollableFrame(root, width=300, height=350, fg_color=Style.color('bg_frame'))
        self.lista_frame.pack(fill="both", expand=True, pady=10, padx=10)

        self.lista_sementes()

        list_sementes = Access.listarSementes()

        sementes_vinculadas = Access.listarSementesFornecedor(self.dados['id'])
        ids_vinculados = {semente['id'] for semente in sementes_vinculadas}

        id_sementes = {"" : None}
        nomes_sementes = [""]

        for semente in list_sementes:
            if semente['id'] not in ids_vinculados:
                id_sementes[semente['nome']] = semente['id']
                nomes_sementes.append(semente['nome'])

        opmenu_var = ctk.StringVar(value='Selecione a Semente')
        en_mtprima_menu = ctk.CTkOptionMenu(root, width=400, height=35, values=nomes_sementes, variable=opmenu_var,
                                            command=lambda choice: self.opcaomenu(id_sementes[choice], opmenu_var), fg_color=Style.color('fg'))
        en_mtprima_menu.pack(padx=10, pady=10)

        bla_frame = Frame(root, bg=Style.color('bg'))
        bla_frame.pack(fill="x", padx=10, pady=10)

        btn_cancelar = ctk.CTkButton(bla_frame, width=190, height=35, text='Cancelar', command=lambda: self.voltar_pagina(root),
                                     fg_color=Style.color('fg'), hover_color=Style.color('hover'))
        btn_cancelar.pack(side=LEFT, padx=10, pady=10)

        btn_cadastrar = ctk.CTkButton(bla_frame, width=190, height=35, text='Adicionar',fg_color=Style.color('fg'), hover_color=Style.color('hover'), command=self.adicionarSemente)
        btn_cadastrar.pack(side=RIGHT, padx=10, pady=10)
    
    def adicionarSemente(self):
        result = Access.editarSementeFornecedor(self.dados['id'],self.semente_selecionada_id)
        if result:
            self.msg_box.showinfo_autoclose(f"Semente adicionada com Sucesso!")
            self.root.destroy()
        else:
            self.msg_box.showinfo_autoclose(f"Erro ao adicionar a semente!")
    
    def delSemente(self,dados):
        op = self.msg_box.askquestion("Confirmação",f"Deseja excluir semente do {self.dados['nome']}?")
        if op == 'yes':
            result = Access.deletarsementeFornecedor(self.dados['id'],dados['id'])
            if result:
                self.msg_box.showinfo_autoclose(f"Semente Excluida com Sucesso!")
                self.root.destroy()
            else:
                self.msg_box.showinfo_autoclose(f"Erro ao excluir a semente!")
        
    def lista_sementes(self):
        
        sementes = Access.listarSementesFornecedor(self.dados['id'])
        
        for i in sementes:
        
            sem_frame = ctk.CTkFrame(self.lista_frame, corner_radius=10)
            sem_frame.pack(fill="x", padx=10, pady=5)

            sem_label = ctk.CTkLabel(sem_frame, text=f"{i['nome']}", font=("Arial", 14))
            sem_label.pack(side="left", pady=5,padx=10)
            btn_del = ctk.CTkButton(sem_frame, text="",image=Style.img('img_icon_delete'),command=lambda dados=i: self.delSemente(dados), width=30,height=30,fg_color=Style.color('fg_red'),hover_color=Style.color('hover_red'))
            btn_del.pack(side="right", padx=5, pady=5)
                
        if not sementes:
            msg_label = ctk.CTkLabel(self.lista_frame, text="Nenhum insumo cadastrado.", font=("Arial", 14))
            msg_label.pack(pady=5)
