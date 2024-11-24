import flet as ft

from menu import Menu
from access import Access

class telaProducao(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.dados = self.obter_dados()

        self.menu = Menu(self.page, active_screen="home")
        self.page.add(self.menu.build())

        self.page.title = "Produção - SkyGreens"
        self.page.padding = 20
        self.page.scroll = "adaptive"

        self.cards_container = ft.Row(spacing=10,wrap=True,alignment=ft.MainAxisAlignment.START)

        self.page.add(self.cards_container)
        self.exibir_prateleiras()

    def obter_dados(self):
        result  = Access.listarProducao()
        return result

    def exibir_prateleiras(self):

        for i in self.dados:

            card = ft.Container(
                width=450,
                height=250,
                padding=10,
                bgcolor="#cdcdcd",
                border=ft.border.all(2, ft.colors.GREY),
                border_radius=10,
                content=ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(f"Semente: {i['nome_semente']}", weight=ft.FontWeight.BOLD, size=30, color="black"),
                                ft.Text(f"Código {i['id']}", size=20, color="black"),
                                ft.Text(f"Status: {i['status']}", size=20, color="black"),
                                ft.Text(f"Quantidade: {i['qtd']}", size=20, color="black"),
                                ft.Text(f"Dias Cultivo: {i['tempoCultivo']}", size=20, color="black"),
                                ft.Text(f"Dias Restantes: {i['diasRestantes']}", size=20, color="black"),   
                            ],
                            spacing=5
                        ),
                        
                        ft.Icon(name=ft.icons.ECO, size=150, color=ft.colors.BLACK)
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=10,
                ),
            )
            self.cards_container.controls.append(card)

        self.page.update()