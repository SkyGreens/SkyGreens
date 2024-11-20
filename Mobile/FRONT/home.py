import flet as ft
import plotly.graph_objects as go
from menu import Menu

class TelaHome(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.menu = Menu(self.page, active_screen="home")
        self.page.add(self.menu.build())

        self.page.title = "Home - SkyGreens"
        self.page.padding = 20
        self.page.scroll = "adaptive"
