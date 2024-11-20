import flet as ft
from access import Access
from home import TelaHome
import asyncio

verde = "#304019"
cinza_escuro = "#212121"
cinza = "#FFFFFF"
bg = "#E7E7E7"

def TelaLogin(page: ft.Page):

    global cpf_input, senha_input, login_message
    
    page.title = "Tela de login"
    page.bgcolor = bg
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    cpf_input = ft.TextField(
        label="CPF",
        width=300,
        text_size=16,
        border_radius=ft.BorderRadius(10, 10, 10, 10),
        filled=True,
        fill_color="#5D732F"
    )
    
    senha_input = ft.TextField(
        label="Senha",
        width=300,
        text_size=16,
        border_radius=ft.BorderRadius(10, 10, 10, 10),
        filled=True,
        password=True,
        fill_color="#5D732F"
    )
    
    login_message = ft.Text(size=16) 
    
    login_button = ft.ElevatedButton(
        text="Entrar",
        on_click=lambda e: on_login_click(page),
        width=300,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=ft.colors.WHITE,
            bgcolor="#304019"
        )
    )
    
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="icon.png", width=20, height=20),
                    ft.Text("Bem-vindo", size=30, color="#4A4A4A", weight=ft.FontWeight.BOLD),
                    ft.Text("Acesse sua conta", size=16, color="#4A4A4A"),
                    ft.Container(height=20),
                    cpf_input,
                    senha_input,
                    ft.Container(height=20),
                    login_button,
                    ft.Container(height=20),
                    login_message,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.Padding(40, 40, 40, 40),
            width=350,
            height=450,
            border_radius=ft.BorderRadius(15, 15, 15, 15),
            bgcolor=ft.colors.WHITE,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(
                blur_radius=15,
                color=ft.colors.BLACK12,
                spread_radius=5
            )
        )
    )
    
    page.update()

def on_login_click(page):
    cpf = cpf_input.value
    senha = senha_input.value
    
    token, userId, message, color = Access.login(cpf, senha)
    
    login_message.value = message
    login_message.color = color
    page.update()

    if token:  # Se o login foi bem-sucedido
        asyncio.run(change_to_home(page, userId, token))  # Passa userId e token


async def change_to_home(page, userId, token):
    await asyncio.sleep(0.1)  # Atraso de 2 segundos
    home_screen = TelaHome(page, userId, token)  # Passa userId e token
    page.clean()  # Limpa a página atual
    home_screen = TelaHome(page, userId, token)  # Passa userId e token
    page.add(home_screen.build())  # Adiciona a tela Home
    page.update()
    