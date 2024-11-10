const url_get_shelves = "http://localhost:8080/skygreen/prateleira/";

async function fetchShelfData(token) {
    try {
        const response = await fetch(url_get_shelves, {  
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }

        const shelvesData = await response.json();
        renderShelves(shelvesData);
    } catch (error) {
        console.error('Erro ao buscar dados de prateleiras:', error);
    }
}

function renderShelves(shelvesData) {
    const container = document.querySelector('.container');
    container.innerHTML = '';  

    shelvesData.forEach(shelf => {
        const shelfCard = document.createElement('div');
        shelfCard.classList.add('card');
        shelfCard.innerHTML = `
            <h2>${shelf.nomePrateleira}</h2>
            <div class="circular-progress">
                <div class="circle">
                    <span>${shelf.diasCrescimento} / ${shelf.cicloTotal} dias</span>
                </div>
            </div>
            <p>${shelf.id}</p>
            <p>${shelf.planta}</p>
            <p><b>Status</b> <i>${shelf.status}</i></p>
        `;
        container.appendChild(shelfCard);
    });
}