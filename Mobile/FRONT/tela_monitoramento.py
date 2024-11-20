import flet as ft

from menu import Menu
from access import Access

class telaMonitoramento(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.dados = self.obter_dados()

        self.menu = Menu(self.page, active_screen="home")
        self.page.add(self.menu.build())

        self.page.title = "Prateleiras - SkyGreens"
        self.page.padding = 20
        self.page.scroll = "adaptive"

        self.cards_container = ft.Row(spacing=10,wrap=True,alignment=ft.MainAxisAlignment.START)

        # Montar layout inicial
        self.page.add(self.cards_container)
        self.exibir_prateleiras()

    def obter_dados(self):
        result = Access.listarPrateleira()
        return result

    def exibir_prateleiras(self):
        # Limpar os cartões existentes
        self.cards_container.controls.clear()

        # Criar novos cartões apenas para as prateleiras com status "Produção"
        for i in self.dados:
            if i['disponivel'] != "Produção":  # Exibe apenas as prateleiras "Produção"
                continue

            card = ft.Container(
                width=280,
                height=200,
                padding=10,
                bgcolor=ft.colors.LIGHT_GREEN,  # Cor para "Produção"
                border=ft.border.all(2, ft.colors.GREEN),  # Cor de borda para "Produção"
                border_radius=10,
                content=ft.Column(
                    [
                        ft.Text(f"Prateleira {i['id']}", weight=ft.FontWeight.BOLD, size=18),
                        ft.Text(f"Status: {i['disponivel']}"),
                        ft.Text(f"Semente: {i['producao']['nome_semente']}" if i["producao"] else "Sem produção"),
                        ft.Text(f"Código: {i['producao']['idseed']}" if i["producao"] else ""),
                    ],
                    spacing=5,
                ),
            )
            self.cards_container.controls.append(card)

        self.page.update()
