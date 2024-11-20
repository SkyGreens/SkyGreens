import flet as ft
from menu import Menu

class telaProducao(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.dados = self.obter_dados()

        # Adicionando o menu à tela
        self.menu = Menu(self.page, active_screen="home")
        self.page.add(self.menu.build())

        # Configurações da página
        self.page.title = "Produção - SkyGreens"
        self.page.padding = 20
        self.page.scroll = "adaptive"

        # Menu suspenso para filtro
        self.filtro_var = ft.Dropdown(
            label="Filtrar por status:",
            options=[
                ft.dropdown.Option("Disponível"),
                ft.dropdown.Option("Produção")
            ],
            value="Produção",
            on_change=self.aplicar_filtro,
        )

        # Espaço para exibição dos cartões
        self.cards_container = ft.Row(
            spacing=10,
            wrap=True,
            alignment=ft.MainAxisAlignment.START
        )

        # Montar layout inicial
        self.page.add(self.filtro_var, self.cards_container)
        self.exibir_prateleiras("Produção")

    def obter_dados(self):
        # Mock de dados, substitua pelo seu método real de acesso aos dados
        return [
            {"id": 1, "disponivel": "Produção", "producao": {"idseed": "123", "nome_semente": "Alface", "graf_valor": [20, 80]}},
            {"id": 2, "disponivel": "Disponível", "producao": None},
            {"id": 3, "disponivel": "Produção", "producao": {"idseed": "124", "nome_semente": "Tomate", "graf_valor": [40, 60]}},
        ]

    def aplicar_filtro(self, e):
        self.exibir_prateleiras(self.filtro_var.value)

    def exibir_prateleiras(self, filtro):
        # Limpar os cartões existentes
        self.cards_container.controls.clear()

        # Criar novos cartões com base no filtro
        for i in self.dados:
            if i['disponivel'] != filtro:
                continue

            card = ft.Container(
                width=280,
                height=200,
                padding=10,
                bgcolor=ft.colors.LIGHT_GREEN if i['disponivel'] == "Disponível" else ft.colors.LIGHT_BLUE,
                border=ft.border.all(2, ft.colors.GREEN if i['disponivel'] == "Disponível" else ft.colors.BLUE),
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

