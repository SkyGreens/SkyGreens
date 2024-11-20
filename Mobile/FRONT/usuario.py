import flet as ft
from menu import Menu
from login import TelaLogin

verde = "#304019"
cinza_escuro = "#212121"
cinza = "#FFFFFF"
bg = "#D6DDC8"

class Usuario(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
        # Inicializa o popup de confirmação
        self.logout_dialog = ft.AlertDialog(
            title=ft.Text("Confirmar Logout", color=cinza_escuro),
            content=ft.Text("Você tem certeza que deseja sair?", color=cinza_escuro),
            actions=[
                ft.TextButton("Cancelar", 
                              on_click=self.cancel_logout,
                              style=ft.ButtonStyle(bgcolor=verde, color=cinza),
                              ),
                ft.TextButton("Sair", 
                              on_click=self.confirm_logout,
                              style=ft.ButtonStyle(bgcolor=verde, color=cinza)
                              ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            bgcolor=bg,
        )

    def show_logout_dialog(self, e):
        """Exibe o popup de confirmação de logout."""
        self.page.dialog = self.logout_dialog
        self.logout_dialog.open = True
        self.page.update()
        
    def confirm_logout(self, e):
        """Confirma o logout e redireciona para a tela de login."""
        self.logout_dialog.open = False
        self.page.update()
        self.page.clean()  # Limpa a tela atual
        TelaLogin(self.page)  # Volta à tela de login
    
    def cancel_logout(self, e):
        """Fecha o popup sem realizar logout."""
        self.logout_dialog.open = False
        self.page.update()

    def build(self):
        # Informações fictícias do usuário
        nome_usuario = "João Silva"
        cargo_usuario = "Admin"
        email_usuario = "joao.silva@example.com"
        
        # Layout da tela de usuário com o menu fixo no topo
        return ft.Column(
            controls=[
                # Menu fixo na parte superior
                ft.Container(
                    content=Menu(self.page, active_screen="usuario").build(),
                    height=60,
                    width=self.page.width,
                    bgcolor=bg,
                    expand=False,
                ),
                
                # Caixa com dados do usuário
                ft.Container(
                    content=ft.Row(
                        controls=[ 
                            ft.Column(
                                controls=[
                                    ft.Image(src="conata.png", width=100, height=100, color=verde),
                                    ft.Text(f"Nome: {nome_usuario}", size=18, color=verde),
                                    ft.Text(f"Cargo: {cargo_usuario}", size=18, color=verde),
                                    ft.Text(f"Email: {email_usuario}", size=18, color=verde),
                                ],
                            ),
                        ],
                        expand=True
                    ),
                    bgcolor=bg,
                    padding=20,
                ),
                
                # Botão de Logout
                ft.ElevatedButton(
                    text="Logout",
                    on_click=self.show_logout_dialog,  # Chama o popup de confirmação
                    bgcolor="#FF0000",
                    width=150,
                    height=45,
                    color="white"
                ),
            ],
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.START,
            expand=True
        )
