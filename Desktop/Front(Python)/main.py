from tkinter import *  # pip install tkinter

from jar import Jar
from style import Style

from telas.tela_login import telaLogin
from telas.tela_base import telaBase
from telas.tela_home import telaHome
from telas.tela_monitoramento import telaMonitoramento
from telas.tela_producao import telaProducao
from telas.tela_pedidos import telaPedidos
from telas.tela_usuario import telaUsuarios
from telas.tela_fornecedor import telaFornecedor
from telas.tela_listaInsumos import listaInsumos
from telas.tela_relatorio import Relatorio
from telas.tela_estoque import Estoque
from telas.tela_pedidoCompra import pedidoCompra
from telas.tela_pedidoVenda import pedidoVenda
from telas.tela_clientes import telaCliente

class Main:
    
    def __init__(self, root):
        self.root = root
        self.telas = {}
        self.tela_atual = None 

        self.tela_login = telaLogin(root, self)
        
    def voltar_para_login(self):
        self.tela_login = telaLogin(self.root, self)

    def iniciar_interface(self,menu_buttons=None):
        if menu_buttons:
            self.menu_buttons = menu_buttons
            self.mostrar_tela("telaHome")
        else:
            self.tela_base = telaBase(root,self)
            self.tela_base.mostrar_tela = self.mostrar_tela
            
            self.mostrar_tela("telaHome")

    def mostrar_tela(self, tela_nome,n=0):
        if self.tela_atual == tela_nome:
            return
        
        if n == 2:
            self.telas["telaMonitoramento"] = telaMonitoramento(root)
        elif n == 3:    
            self.telas["telaFornecedor"] = telaFornecedor(root)
        elif n == 4:
            self.telas["telaProducao"] = telaProducao(root,self)
        elif n == 5:
            self.telas["telaPedidos"] = telaPedidos(root,self)
        elif n == 6:
            self.telas["telaUsuarios"] = telaUsuarios(root)
        elif n == 7:
            self.telas["Relatorio"] = Relatorio(root,self)
        elif n == 8:
            self.telas["Estoque"] = Estoque(root,self)
        elif n == 9: 
            self.telas["listaInsumos"] = listaInsumos(root,self)
        elif n == 10:
            self.telas["pedidoCompra"] = pedidoCompra(root,self)
        elif n == 11:
            self.telas["pedidoVenda"] = pedidoVenda(root,self)
        elif n == 12:
            self.telas["telaCliente"] = telaCliente(root,self)
        elif n == 0:
            self.telas["telaHome"] = telaHome(root,self,self.menu_buttons)
        
        for tela in self.telas.values():
            tela.esconder()
        self.telas[tela_nome].mostrar()
        
        self.tela_atual = tela_nome
            
if __name__ == "__main__":
    jar_instance = Jar()
    root = Tk()
    root.title("SkyGreens")
    root.configure(background=Style.color('bg'))

    largura_janela = 1300
    altura_janela = 640

    Style.centralizar_janela(root, largura_janela, altura_janela)

    app = Main(root)
    root.mainloop()