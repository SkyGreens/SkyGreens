import flet as ft

from menu import Menu
from access import Access

class TelaHome(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.menu = Menu(self.page, active_screen="home")
        self.page.add(self.menu.build())
        self.page.title = "Home - SkyGreens"
        self.page.padding = 20
        self.page.scroll = "adaptive"

        self.page.add(ft.Column([self._build_cards()],alignment="center",horizontal_alignment="center",spacing=20))
        self.page.update()

    def _build_cards(self):

        card_pedidos = self._build_card(title="Pedidos",description=self.listarPedidos(),icon=ft.icons.SHOPPING_CART,bgcolor=ft.colors.GREEN_50)

        card_producao = self._build_card(title="Produção",description=self.producaoAtiva(),icon=ft.icons.AGRICULTURE,bgcolor=ft.colors.LIGHT_GREEN_50)

        card_estoque = self._build_card(title="Estoque",description=self.buscarEstoque(),icon=ft.icons.INVENTORY,bgcolor=ft.colors.YELLOW_50)

        card_prateleiras = self._build_card(title="Prateleiras",description=self.listarPrateleira(),icon=ft.icons.STORAGE,bgcolor=ft.colors.BLUE_50)

        return ft.Column([card_pedidos, card_producao, card_estoque, card_prateleiras],spacing=20,alignment="center",horizontal_alignment="center")

    def buscarEstoque(self):
        result = Access.listarEstoque()
        estoque = ""

        for item in result:
            nome = item['nome_semente']
            qtd = item['qtd']
            estoque += f"{nome}: {qtd}\n"
            
        return estoque

    def listarPrateleira(self):
        
        result = Access.listarPrateleira()
        
        prateleiras_disponiveis = 0
        prateleiras_producao = 0

        for item in result:
            if item['disponivel'] == 'Produção':
                prateleiras_producao += 1
            else:
                prateleiras_disponiveis += 1


        prateleiras_info = f"Prateleiras Disponíveis: {prateleiras_disponiveis} \nPrateleiras Alocadas: {prateleiras_producao}"
        return prateleiras_info
    
    def listarPedidos(self):
        result = Access.listarpedidosVenda()
        total_pedidos = len(result)
        return f"Pedidos de venda: {total_pedidos}"
    
    def producaoAtiva(self):
        result = Access.listarProducao()
        total = 0
        for item in result:
            if item['status'] == 'Ativo':
                total += item['qtd']
        return f"Total de itens em produção: {total}"
    
    def _build_card(self, title, description, icon, bgcolor):

        return ft.Container(width=420,height=150,bgcolor=bgcolor,border_radius=ft.border_radius.all(15),padding=10,
            content=ft.Column([
                    ft.Row([
                            ft.Icon(name=icon, size=40, color=ft.colors.GREEN),
                            ft.Text(title, size=18, weight="bold", color=ft.colors.BLACK)],
                        alignment="spaceBetween"
                    ),
                    ft.Text(description, size=14, color=ft.colors.BLACK54)],
                spacing=10))
