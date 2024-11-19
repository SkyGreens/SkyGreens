import flet as ft
from access import Access
from menu import Menu

verde = "#304019"
cinza_escuro = "#212121"
cinza = "#FFFFFF"
bg = "#D6DDC8"

class Pedidos(ft.UserControl):
    def __init__(self, page, userId, token):
        super().__init__()
        self.page = page
        self.userId = userId
        self.token = token
        self.pedidos = []  # Lista inicial vazia para os pedidos
        self.pesq_conteudo = ft.TextField(label="Pesquisar Venda", autofocus=True)

    def carregar_pedidos(self):
        try:
            api = Access(self.token)
            self.pedidos = api.obter_pedidos()  # Usando o método para obter os pedidos da API
        except Exception as e:
            print("ERRO!")
            self.page.update()

    def pesquisar_pedidos(self, event):
        termoPesq = self.pesq_conteudo.value.lower()
        pedidos_filtrados = [pedido for pedido in self.pedidos if termoPesq in pedido['produto'].lower() or termoPesq in pedido['cliente'].lower()]
        
        return pedidos_filtrados

    def build(self):
        # Carrega os pedidos ao construir a tela
        self.carregar_pedidos()

        # Retorna a estrutura da página com o menu no topo e os pedidos abaixo
        return ft.Column(
            controls=[
                Menu(self.page, self.userId, self.token, active_screen="pedidos").build(),  # Menu fixo
                self.pesq_conteudo,  # Campo de pesquisa
                self.retangulo_pedidos(),  # Exibe os pedidos
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def retangulo_pedidos(self):
        # Cria os textos dinamicamente para cada pedido da API
        pedidos_controls = []
        pedidos_filtrados = self.pesquisar_pedidos(None)  # Aplica o filtro com base na pesquisa
        
        if pedidos_filtrados:
            for pedido in pedidos_filtrados:
                texto = f"Pedido ID: {pedido.get('id')} - Produto: {pedido.get('produto')} - Quantidade: {pedido.get('quantidade')} - Cliente: {pedido.get('cliente')}"
                pedidos_controls.append(ft.Text(texto, color=cinza_escuro))
        else:
            pedidos_controls.append(ft.Text("Nenhum pedido encontrado.", color=verde))
        
        # Retorna o container com os pedidos
        return ft.Container(
            content=ft.Column(
                controls=pedidos_controls,
                alignment=ft.MainAxisAlignment.START,
            ),
            bgcolor=bg,
            padding=20,
            margin=ft.margin.all(10),
            border_radius=10,
            expand=True,
            alignment=ft.alignment.center,
            width=350,
        )
