import flet as ft

verde = "#304019"
cinza = "#FFFFFF"
bg = "#D6DDC8"

class Menu(ft.UserControl):
    def __init__(self, page, active_screen):
        super().__init__()
        self.page = page
        self.active_screen = active_screen

        self.menu_container = ft.Container(
            content=ft.Row(
                controls=[
                    ft.TextButton(text="Home", on_click=self.go_to_home, style=ft.ButtonStyle(bgcolor="#5D732F", color=cinza)),
                    ft.TextButton(text="Prateleira", on_click=self.go_to_monit, style=ft.ButtonStyle(bgcolor="#5D732F", color=cinza)),
                    ft.TextButton(text="Produção", on_click=self.go_to_prod, style=ft.ButtonStyle(bgcolor="#5D732F", color=cinza)),
                    ft.TextButton(text="Pedidos", on_click=self.go_to_pedidos, style=ft.ButtonStyle(bgcolor="#5D732F", color=cinza)),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=self.page.width,height=100,bgcolor=verde,padding=10,opacity=0,visible=False,)

    def toggle_menu(self, e):
        self.menu_container.visible = not self.menu_container.visible
        self.menu_container.opacity = 0.9 if self.menu_container.visible else 0
        self.page.update()

    def go_to_home(self, e):
        self.page.controls.clear()
        from telas.tela_home import TelaHome
        home_screen = TelaHome(self.page)
        self.page.add(home_screen)
        self.page.update()

    def go_to_monit(self, e):
        self.page.controls.clear()
        from telas.tela_monitoramento import telaMonitoramento
        monit_screen = telaMonitoramento(self.page)
        self.page.add(monit_screen)
        self.page.update()

    def go_to_prod(self, e):
        self.page.controls.clear()
        from telas.tela_producao import telaProducao
        prod_screen = telaProducao(self.page)
        self.page.add(prod_screen)
        self.page.update()

    def go_to_usuario(self, e):
        self.page.controls.clear()
        from telas.perfil_user import Usuario
        usuario_screen = Usuario(self.page)
        self.page.add(usuario_screen.build())
        self.page.update()

    def go_to_pedidos(self, e):
        self.page.controls.clear()
        from telas.tela_pedidos import Pedidos
        pedidos_screen = Pedidos(self.page)
        self.page.add(pedidos_screen)
        self.page.update()

    def build(self):
        top_row = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(ft.icons.MENU, on_click=self.toggle_menu, icon_color=cinza),
                    ft.IconButton(ft.icons.ACCOUNT_CIRCLE, on_click=self.go_to_usuario, icon_color=cinza),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                expand=True,
            ),
            bgcolor=verde,padding=15,width=self.page.width,)
        
        
        return ft.Column([top_row, self.menu_container])