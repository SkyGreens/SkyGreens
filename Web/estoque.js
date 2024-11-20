const url_get_stocks = "http://localhost:8080/skygreen/estoque/";

async function fetchStock(token) {
    try {
        const response = await fetch(url_get_stocks, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }

        const stocks = await response.json();

        renderstocks(stocks);
    } catch (error) {
        console.error('Erro ao buscar stocks:', error);
    }
}

function renderstocks(stocks) {
    const stocksList = document.getElementById('stocks-list');
    stocksList.innerHTML = ''; 
    console.log(stocks);

    stocks.forEach(stock => {
        const stockCard = document.createElement('div');
        stockCard.classList.add('stock-card');
        stockCard.innerHTML = `
            <p><strong>ID:</strong> ${stock.estoqueId}</p>
            <p><strong>Quantidade:</strong> ${stock.quantidade}</p>
            <p><strong>Semente:</strong> ${stock.semente.sementeId}</p>
        `;
        stocksList.appendChild(stockCard);
    });
}