import flet as ft
from login import TelaLogin  # Importa a classe Login
from home import TelaHome

def main(page: ft.Page):
    TelaLogin(page)  # Instancia a classe Login, passando a página

    # Define o tamanho da janela
    page.window_width = 400
    page.window_height = 700
    
    # Configurações adicionais da página
    page.title = "SkyGreens"
    page.window_resizable = False  # Para não permitir redimensionamento

    # Atualiza a página para aplicar as alterações
    page.update()
    page.favicon = "LOGOO.ico"  # Apenas para teste

# Executa a aplicação
ft.app(target=main)
