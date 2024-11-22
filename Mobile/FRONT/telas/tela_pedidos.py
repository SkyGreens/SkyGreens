import flet as ft
from menu import Menu
from access import Access

class Pedidos(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.pedidos = Access.listarpedidosVenda()

        self.menu = Menu(self.page, active_screen="home")
        self.page.add(self.menu.build())

        self.page.title = "Pedidos - SkyGreens"
        self.page.padding = 20
        self.page.scroll = "adaptive"
        
        search_box = ft.TextField(label="Pesquisar", on_change=lambda e: self.update_list(e.control.value), color="black")
        
        self.item_list = ft.Column(expand=True)
        self.display_pedidos()
        self.page.add(search_box, self.item_list)

    def display_pedidos(self):
        self.item_list.controls.clear()
        for pedido in self.pedidos:
            cliente = pedido['cliente']
            semente = pedido['semente']
            
            pedido_card = ft.Container(width=450,height=50,padding=10,bgcolor="#cdcdcd",
                border=ft.border.all(2, ft.colors.GREY),
                border_radius=10,
                content=ft.Column([ft.Text(f"Cliente: {cliente['razaoSocial']} - Quantidade: {pedido['qtd']} - Semente: {semente['nome']}", color="black", size=14)],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=10
                )
            )
            self.item_list.controls.append(pedido_card)
        
        self.page.update()

    def update_list(self, query):
        if not query:
            self.pedidos = Access.listarpedidosVenda()
        else:
            self.pedidos = [pedido for pedido in self.pedidos 
                if query.lower() in pedido['semente']['nome'].lower() 
                or query.lower() in pedido['cliente']['razaoSocial'].lower()
            ]
        self.display_pedidos()

