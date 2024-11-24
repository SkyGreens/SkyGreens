import flet as ft
from menu import Menu
from access import Access
from telas.tela_login import TelaLogin

verde = "#304019"
cinza_escuro = "#212121"
cinza = "#FFFFFF"
bg = "#D6DDC8"

class Usuario(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
        self.menu = Menu(self.page, active_screen="home")
        self.page.add(self.menu.build())

        self.logout_dialog = ft.AlertDialog(
            title=ft.Text("Confirmar Logout", color=cinza_escuro),
            content=ft.Text("Você tem certeza que deseja sair?", color=cinza_escuro),
            actions=[
                ft.TextButton("Cancelar", 
                              on_click=self.cancel_logout,
                              style=ft.ButtonStyle(bgcolor=verde, color=cinza)),
                ft.TextButton("Sair", 
                              on_click=self.confirm_logout,
                              style=ft.ButtonStyle(bgcolor=verde, color=cinza)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            bgcolor=bg,
        )

    def show_logout_dialog(self, e):
        self.page.dialog = self.logout_dialog
        self.logout_dialog.open = True
        self.page.update()
        
    def confirm_logout(self, e):
        self.logout_dialog.open = False
        
        self.page.controls.clear() 
        from telas.tela_login import TelaLogin
        self.page.add(TelaLogin(self.page))
        self.page.update()
    
    def cancel_logout(self, e):
        self.logout_dialog.open = False
        self.page.update()

    def build(self):
        
        result = Access.visualizarPerfil()
        user_data = result[0] if result else {}

        nome_usuario = user_data.get("nome", "N/A")
        cargo_usuario = user_data.get("cargo", "N/A")
        email_usuario = user_data.get("email", "N/A")
        cpf_usuario = user_data.get("cpf", "N/A")
        status_usuario = "Ativo" if user_data.get("ativo", False) else "Inativo"

        return ft.Column(
            controls=[
                
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Icon(name="person", size=100, color=verde),
                                width=150,
                                height=150,
                                bgcolor=bg,
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(f"Nome: {nome_usuario}", size=20, color=verde),
                                        ft.Text(f"Cargo: {cargo_usuario}", size=16, color=verde),
                                        ft.Text(f"E-mail: {email_usuario}", size=16, color=verde),
                                        ft.Text(f"CPF: {cpf_usuario}", size=16, color=verde),
                                        ft.Text(f"Status: {status_usuario}", size=16, color=verde),
                                        ft.Text(f"Empresa: SkyGreens", size=16, color=verde),
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                bgcolor=bg,
                                alignment=ft.alignment.center,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    bgcolor=bg,
                    expand=True,
                    padding=ft.Padding(20, 20, 20, 40),

                ),

                ft.Container(height=30),

                ft.Container(
                    content=ft.ElevatedButton(
                        text="Logout",
                        on_click=self.show_logout_dialog,
                        bgcolor="#D32F2F",
                        color="#FFFFFF",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            text_style=ft.TextStyle(size=24)
                            ),
                        height=60,
                        width=200,
                ),
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        )
