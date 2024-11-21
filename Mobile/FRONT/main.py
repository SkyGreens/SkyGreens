import flet as ft
import subprocess

from jar import Jar 
from telas.tela_login import TelaLogin 

def main(page: ft.Page):
    
    Jar()
    TelaLogin(page)
    
    page.window.width = 500
    page.window.height = 800
    
    page.title = "SkyGreens"
    page.window.resizable = False

    page.update()
    page.window_close() #PARA FECHAR A JANELA NO COMPUTADOR
    subprocess.run(["flet", "run", "main.py", "--android"]) #PARA RODAR O ANDROID NO FLET

ft.app(target=main)