import customtkinter as ctk # pip install customtkinter

from style import Style,MessageBox
from access import Access

class cdInsumos:
    
    def __init__(self,callback,dados=None,editar=None):
        self.jn_x = 640
        self.jn_y = 180
        
        self.callback = callback
        self.dados = dados
        self.editar = editar
        
        titulo = ("Consultar Insumo" if self.editar == 0 else "Editar Insumo" if self.editar == 1 else "Cadastrar Insumo")
        self.root = Style.criar_janela_flutuante(titulo, self.jn_x, self.jn_y)
        self.elementos_tela(self.root)
        self.root.mainloop()

    def voltar_pagina(self, root):
        root.destroy()

    def atualizar_pagina(self,i=0):
        self.root.destroy()
        self.dados = None
        if i == 1:
            from tela_listaInsumos import listaInsumos
            listaInsumos.sementes_lista(self.callback)
    
    def modificacao_semente(self,nome,desc):
        msg_box = MessageBox()
        
        #if self.dados: editar
            #result = Access.editarFornecedor(self.dados['id'], status, email, tel, end, cid, est, pais, isced, rzsocial, cnpj, semente)
        
        result = Access.cadastrarSementes(nome,desc)
        if result:
            msg_box.showinfo_autoclose(f"Insumo cadastrado com sucesso!")
        else:
            msg_box.showinfo_autoclose(f"Insumo não cadastrado!")
        
        
        if result:
            self.atualizar_pagina(1)
    
    def elementos_tela(self, root):
        
        estado_campo = "normal" if self.editar != 0 else "disabled"
        
        #(placeholder, nome do campo, linha, coluna)
        self.campos = [("Nome", "nome", 0),("Descrição", "descricao", 1)]
        self.widgets = {}
        
        for (placeholder, comp_nome, row, *column) in self.campos:
            col = column[0] if column else 0

            self.widgets[comp_nome] = ctk.CTkEntry(root, width=620 if not column else 300, height=35, placeholder_text=placeholder)

            if self.dados and comp_nome in self.dados:
                valor = self.dados[comp_nome]
                if valor:
                    self.widgets[comp_nome].insert(0, valor)

            self.widgets[comp_nome].configure(state=estado_campo)
            self.widgets[comp_nome].grid(row=row, column=col, columnspan=2 if not column else 1, padx=10, pady=10)
        
        #==
        
        if self.editar != 0:
            btn_cancelar = ctk.CTkButton(root, width=300, height=35, text='Cancelar',
                                         command=lambda: self.voltar_pagina(root), fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_cancelar.grid(row=6, column=0, padx=10, pady=10)

            btn_texto = 'Atualizar' if self.dados else 'Cadastrar'
            btn_registrar = ctk.CTkButton(root, width=300, height=35, text=btn_texto, command=lambda: self.modificacao_semente(self.widgets['nome'].get(),self.widgets['descricao'].get()), fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_registrar.grid(row=6, column=1, padx=10, pady=10)
        else:
            btn_ok = ctk.CTkButton(root, width=300, height=35, text='Ok', command=lambda: self.voltar_pagina(root), fg_color=Style.color('fg'), hover_color=Style.color('hover'))
            btn_ok.grid(row=6, column=0, columnspan=2, padx=10, pady=10)