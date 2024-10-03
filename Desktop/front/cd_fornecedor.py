import customtkinter as ctk # pip install customtkinter
from tkinter import Toplevel # pip install tkinter

from access import Access

fg = "#3ab355"  # menu
hover = "#316133"  # hover/principal
bg = "#dfeedf"  # background

class cdFornecedor:
    def __init__(self):
        jn_x = 640
        jn_y = 560
        root = Toplevel()
        root.title("Cadastrar Fornecedor")
        root.geometry(f"{jn_x}x{jn_y}")
        root.wm_attributes('-toolwindow', 1)
        root.configure(background='#dfeedf')

        #ctk.set_appearance_mode("light")
        
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
    
    def cadastrar_fornecedor(self, cnpj, rzsocial, isced, email, status, tel, end, cid, est, pais):
        status = False if status == "Inativo" else True
        print(f"Fornecedor Cadastrado\nRazão Social: {rzsocial}\nStatus: {status}")
        #Access.cadatroFornecedor(status, email, tel, end, cid, est, pais, isced, rzsocial, cnpj)

    def voltar_pagina(self, root):
        root.destroy()

    def switch(self, switch_var):
        switch_var.set("Inativo")

    def opcaomenu(self, choice, opmenu_var):
        if choice == "Adicionar":
            opmenu_var.set('Materia Prima')
            print('Adicionado!')
        elif choice == "":
            opmenu_var.set('Materia Prima')
        else:
            print("Opção Menu clicada:", choice)

    def elementos_tela(self, root):
        campos = [
            ('CNPJ', 0), ('Razão Social', 1), ('Inscrição Estadual', 2), ('E-mail', 3),
            ('Endereço', 4), ('Cidade', 5), ('Telefone', 6, 0), ('Estado', 6, 1), ('País', 7, 0)
        ]
        
        widgets = {}
        for (placeholder, row, *column) in campos:
            col = column[0] if column else 0
            widgets[placeholder.lower()] = ctk.CTkEntry(root, width=620 if not column else 300, height=35, placeholder_text=placeholder)
            widgets[placeholder.lower()].grid(row=row, column=col, columnspan=2 if not column else 1, padx=10, pady=10)

        switch_var = ctk.StringVar(value="Ativo")
        widgets['status'] = ctk.CTkSwitch(root, textvariable=switch_var, width=300, height=35, variable=switch_var, onvalue="Ativo", offvalue="Inativo")
        widgets['status'].grid(row=7, column=1, padx=10, pady=10)

        list_sementes = ["", "Alface", "Tomate", "Adicionar"]
        opmenu_var = ctk.StringVar(value='Materia Prima')
        en_mtprima_menu = ctk.CTkOptionMenu(root, width=620, height=35, values=list_sementes, variable=opmenu_var, command=lambda choice: self.opcaomenu(choice, opmenu_var))
        en_mtprima_menu.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar', command=lambda: self.voltar_pagina(root))
        btn_cancelar.grid(row=9, column=0, padx=10, pady=10)

        btn_registrar = ctk.CTkButton(root, width=300, height=35, text='Registrar', command=lambda: self.cadastrar_fornecedor(
            widgets['cnpj'].get(), widgets['razão social'].get(), widgets['inscrição estadual'].get(), widgets['e-mail'].get(),
            widgets['status'].get(), widgets['telefone'].get(), widgets['endereço'].get(), widgets['cidade'].get(), widgets['estado'].get(), widgets['país'].get()
        ))
        btn_registrar.grid(row=9, column=1, padx=10, pady=10)