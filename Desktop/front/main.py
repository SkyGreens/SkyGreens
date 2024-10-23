from tkinter import *  # pip install tkinter

from jar import Jar
from style import Style

from tela_login import telaLogin
from tela_base import telaBase
from tela_home import telaHome
from tela_monitoramento import telaMonitoramento
from tela_producao import telaProducao
from tela_pedidos import telaPedidos
from tela_usuario import telaUsuarios
from tela_fornecedor import telaFornecedor
from tela_listaInsumos import listaInsumos
from tela_relatorio import Relatorio
from tela_estoque import Estoque

class Main:
    
    def __init__(self, root):
        self.root = root
        self.telas = {}

        self.tela_login = telaLogin(root, self)

    def iniciar_interface(self):

        self.tela_base = telaBase(root)
        self.tela_base.mostrar_tela = self.mostrar_tela

        self.telas["telaHome"] = telaHome(root,self)
        self.telas["telaMonitoramento"] = telaMonitoramento(root)
        self.telas["telaFornecedor"] = telaFornecedor(root)
        self.telas["telaProducao"] = telaProducao(root,self)
        self.telas["telaPedidos"] = telaPedidos(root)
        self.telas["telaUsuarios"] = telaUsuarios(root)
        self.telas["listaInsumos"] = listaInsumos(root,self)
        self.telas["Relatorio"] = Relatorio(root,self)
        self.telas["Estoque"] = Estoque(root,self)

        self.mostrar_tela("telaHome")

    def mostrar_tela(self, tela_nome):
                
        for tela in self.telas.values():
            tela.esconder()
        if tela_nome in self.telas:
            self.telas[tela_nome].mostrar()

if __name__ == "__main__":
    jar_instance = Jar()
    root = Tk()
    root.title("SkyGreens")
    root.configure(background=Style.color('bg'))

    largura_janela = 1300
    altura_janela = 600

    Style.centralizar_janela(root, largura_janela, altura_janela)

    app = Main(root)
    root.mainloop()
