async function fetchProductionData(token) {
    try {
        const response = await fetch(url_get_production, {  
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }

        const productionData = await response.json();
        renderProduction(productionData);
    } catch (error) {
        console.error('Erro ao buscar dados de produção:', error);
    }
}

function renderProduction(productionData) {
    const prodGrid = document.querySelector('.prod-grid');
    prodGrid.innerHTML = '';  

    productionData.forEach(prodItem => {
        const itemDiv = document.createElement('div');
        itemDiv.classList.add('prod-item');
        itemDiv.innerHTML = `
            <p>ID: ${prodItem.producaoId}</p>
            <p>Semente ID: ${prodItem.sementeId}</p>
            <p>Quantidade: ${prodItem.sementeQuantidade}</p>
            <p>Tempo de cultivo: ${prodItem.tempoCultivo}</p>
            <p>Data inicial: ${prodItem.dataInicio.split('T')[0]}</p>
        `;
        prodGrid.appendChild(itemDiv);
    });
}