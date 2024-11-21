import flet as ft

def main(page):
    # Lista de itens
    items = [
        "Cenoura", "Batata", "Tomate", "Alface", "Pepino", 
        "Abobrinha", "Cebola", "Alho", "Pimentão", "Rúcula"
    ]
    
    # Caixa de pesquisa
    search_box = ft.TextField(
        label="Pesquisar", 
        on_change=lambda e: update_list(e.control.value, items)
    )
    
    # Lista para exibir os itens
    item_list = ft.Column(
        expand=True,
        controls=[ft.Text(item) for item in items]
    )
    
    # Função para atualizar a lista com base na pesquisa
    def update_list(query, items):
        filtered_items = [item for item in items if query.lower() in item.lower()]
        item_list.controls = [ft.Text(item) for item in filtered_items]
        page.update()

    # Layout da tela
    page.add(search_box, item_list)

# Executa o aplicativo Flet
ft.app(target=main)
