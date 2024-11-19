import flet as ft

verde = "#304019"
cinza_escuro = "#212121"
cinza = "#FFFFFF"
bg = "#D6DDC8"

class Menu(ft.UserControl):
    def __init__(self, page, userId, token, active_screen):
        super().__init__()
        self.page = page
        self.userId = userId  # Armazena o ID do usuário
        self.token = token     # Armazena o token
        self.active_screen = active_screen


    def go_to_home(self, e):
        self.page.clean()  # Limpa a tela atual
        from home import TelaHome  # Importa a tela Home
        home_screen = TelaHome(self.page, self.userId, self.token)  # Passa userId e token
        self.page.add(home_screen.build())  # Adiciona a tela Home à página
        self.page.update()  # Atualiza a página

    def go_to_usuario(self, e):
        self.page.clean()  # Limpa a tela atual
        from usuario import Usuario  # Importa a tela de Usuário
        usuario_screen = Usuario(self.page, self.userId, self.token)  # Passa userId e token
        self.page.add(usuario_screen.build())  # Adiciona a tela Usuário à página
        self.page.update()  # Atualiza a página

    def go_to_pedidos(self, e):
        self.page.clean()  # Limpa a tela atual
        from pedidos import Pedidos  # Importa a tela Pedidos
        pedidos_screen = Pedidos(self.page, self.userId, self.token)  # Passa userId e token
        self.page.add(pedidos_screen.build())  # Adiciona a tela Pedidos à página
        self.page.update()  # Atualiza a página

    def build(self):
        
        home_button_color = "#1D260F" if self.active_screen == "home" else "#5D732F"
        pedidos_button_color = "#1D260F" if self.active_screen == "pedidos" else "#5D732F"
        usuario_button_color = "#1D260F" if self.active_screen == "usuario" else "#5D732F"
        # Criação da barra de menu na parte inferior da tela
        menu_barra_inferior = ft.Container(
            content=ft.Row(
                controls=[
                    ft.TextButton(
                        text="Monitoramento", 
                        on_click=self.go_to_home, 
                        style=ft.ButtonStyle(bgcolor=home_button_color, color=cinza)
                    ),
                    ft.TextButton(
                        text="Pedidos", 
                        on_click=self.go_to_pedidos, 
                        style=ft.ButtonStyle(bgcolor=pedidos_button_color, color=cinza)
                    ),
                    ft.TextButton(
                        text="Perfil", 
                        on_click=self.go_to_usuario, 
                        style=ft.ButtonStyle(bgcolor=usuario_button_color, color=cinza)
                    ),
                    ft.Image(src="icon.png", width=30, height=30,),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=10,
            bgcolor=verde,
            height=60
        )

        return menu_barra_inferior
