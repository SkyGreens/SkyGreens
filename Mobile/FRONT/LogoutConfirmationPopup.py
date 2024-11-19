import flet as ft

class LogoutConfirmationPopup:
    def __init__(self, page, callback):
        self.page = page
        self.callback = callback
        self.dialog = ft.AlertDialog(
            title="Confirmação de Logout",
            content=ft.Text("Você tem certeza que deseja sair?"),
            actions=[
                ft.ElevatedButton("Cancelar", on_click=self.close),
                ft.ElevatedButton("Confirmar", on_click=self.confirm_logout)
            ]
        )

    def show(self):
        # Exibe o popup de confirmação
        self.page.add(self.dialog)
        self.page.update()

    def close(self, e):
        # Fecha o popup sem fazer logout
        self.page.remove(self.dialog)
        self.page.update()

    def confirm_logout(self, e):
        # Executa o callback de logout e fecha o popup
        self.callback()
        self.page.remove(self.dialog)
        self.page.update()
