import flet as ft
from menu import Menu
import plotly.graph_objects as go
import plotly.io as pio
from PIL import Image
import io

verde = "#304019"
cinza_escuro = "#212121"
cinza = "#FFFFFF"
bg = "#D6DDC8"


class TelaHome(ft.UserControl):
    def __init__(self, page, userId, token):
        super().__init__()
        self.page = page
        self.userId = userId
        self.token = token

    def build(self):
        # Cria o conteúdo principal da tela Home com o gráfico de barras
        conteudo_principal = ft.Row(
            controls=[
                self.grafico_barra(),  # Adiciona o gráfico de barras à tela
            ],
            expand=True,  # Garante que o conteúdo principal ocupe o espaço disponível
            alignment=ft.MainAxisAlignment.CENTER, # Centraliza o conteúdo na tela
        )

        # Retorna a estrutura da página com o menu no topo e o gráfico abaixo
        return ft.Column(
            controls=[
                Menu(self.page, self.userId, self.token, active_screen="home").build(),  # Menu fixo na parte superior
                conteudo_principal,  # Gráfico abaixo do menu
            ],
            expand=True  # Garante que a coluna ocupe todo o espaço da página
        )

    def grafico_barra(self):
        # Exemplo de dados para o gráfico de barras
        prateleiras = ['Prateleira 1', 'Prateleira 2', 'Prateleira 3', 'Prateleira 4']
        dias_passados = [10, 0, 0, 2]  # Dados fictícios
        dias_restantes = [5, 0, 12, 5]  # Dados fictícios

        # Criando o gráfico de barras
        fig = go.Figure(data=[
            go.Bar(name='Dias Passados', x=prateleiras, y=dias_passados, marker_color='blue'),
            go.Bar(name='Dias Restantes', x=prateleiras, y=dias_restantes, marker_color='green')
        ])

        fig.update_layout(
            title='',
            barmode='stack',  # Pilha de barras
            xaxis_title='',
            yaxis_title='',
            template='simple_white',  # Estilo escuro
            width=550,  # Ajuste de largura do gráfico para caber bem na tela
            height=650
        )

        # Salvando o gráfico como imagem em memória
        img_bytes = pio.to_image(fig, format='png')

        # Convertendo os bytes para uma imagem que o Flet pode exibir
        img = Image.open(io.BytesIO(img_bytes))
        img_path = "monitoramento_grafico.png"
        img.save(img_path)

        # Adicionando o gráfico (imagem) à tela
        return ft.Column(
            controls=[
                ft.Text("Producao", size=20, color=verde, text_align=ft.TextAlign.CENTER),
                ft.Image(src=img_path, width=350, height=450)  # Exibe a imagem do gráfico
            ],
        )
