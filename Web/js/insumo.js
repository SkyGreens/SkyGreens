async function fetchInsumos(token) {
    try {
        const response = await fetch(url_get_insumos, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }

        const insumos = await response.json();

        renderInsumos(insumos);
    } catch (error) {
        console.error('Erro ao buscar insumos:', error);
    }
}

function renderInsumos(insumos) {
    const insumosList = document.getElementById('insumos-list');
    insumosList.innerHTML = ''; 
    console.log(insumos);

    insumos.forEach(insumo => {
        const insumoCard = document.createElement('div');
        insumoCard.classList.add('insumo-card');
        insumoCard.innerHTML = `
            <h3>Insumo: ${insumo.nome}</h3>
            <p><strong>Descrição:</strong> ${insumo.descricao}</p>
            <p><strong>ID:</strong> ${insumo.sementeId}</p>
        `;
        insumosList.appendChild(insumoCard);
    });
}