import flet as ft
import subprocess

from jar import Jar 
from login import TelaLogin 

def main(page: ft.Page):
    
    Jar()
    TelaLogin(page)
    
    page.window.width = 500
    page.window.height = 800
    
    page.title = "SkyGreens"
    page.window.resizable = False

    page.update()
    #page.window_close()
    #subprocess.run(["flet", "run", "main.py", "--android"])

ft.app(target=main)