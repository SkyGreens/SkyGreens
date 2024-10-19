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

class Main:
    def __init__(self, root):
        self.root = root
        self.telas = {}

        self.tela_login = telaLogin(root, self)

    def iniciar_interface(self):

        self.tela_base = telaBase(root)
        self.tela_base.mostrar_tela = self.mostrar_tela

        self.telas["telaHome"] = telaHome(root, self)
        self.telas["telaMonitoramento"] = telaMonitoramento(root)
        self.telas["telaFornecedor"] = telaFornecedor(root)
        self.telas["telaProducao"] = telaProducao(root)
        self.telas["telaPedidos"] = telaPedidos(root)
        self.telas["telaUsuarios"] = telaUsuarios(root)

        self.mostrar_tela("telaHome")

    def mostrar_tela(self, tela_nome):
        for tela in self.telas.values():
            tela.esconder()

        self.telas[tela_nome].mostrar()

    def retornar_login(self):
        self.tela_login = telaLogin(self.root, self)

if __name__ == "__main__":
    jar_instance = Jar()
    root = Tk()
    root.title("SkyGreens")
    root.configure(background=Style.color('bg'))

    largura_janela = 1300
    altura_janela = 600

    def centralizar_janela(root, largura, altura):

        tela_largura = root.winfo_screenwidth()
        tela_altura = root.winfo_screenheight()

        x = (tela_largura // 2) - (largura // 2)
        y = (tela_altura // 2) - (altura // 2)

        root.geometry(f"{largura}x{altura}+{x}+{y}")

    centralizar_janela(root, largura_janela, altura_janela)

    app = Main(root)
    root.mainloop()
