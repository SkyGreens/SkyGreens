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
    console.log(shelvesData);

    shelvesData.forEach(shelf => {
        const shelfCard = document.createElement('div');
        shelfCard.classList.add('card');
    
        let daysPassed, totalDays, progress, status, semente;
    
        if (isProducaoDisponivel(shelf.producao)) {
            daysPassed = calculateDaysPassed(shelf.producao.dataInicio);
            totalDays = calculateTotalDays(shelf.producao.dataInicio, shelf.producao.dataFim);
            progress = calculateProgress(shelf.producao.dataInicio, shelf.producao.dataFim);
            status = calculateStatus(shelf.producao.dataFim);
            semente = shelf.producao.sementeId;
        } else {
            daysPassed = "?";
            totalDays = "?";
            progress = "Indisponível";
            status = "Indisponível";
            semente = "Indisponível";
        }
    
        // Preenchendo o conteúdo do card
        shelfCard.innerHTML = `
            <h2>${shelf.nome}</h2>
            <div class="circular-progress">
                <div class="circle">
                    <span>${daysPassed} / ${totalDays} dias </span>
                </div>
                <div class="progress-bar-container">
                    <div class="progress-bar" style="width: ${progress}%"></div>
                </div>
            </div>
            <p>ID: ${shelf.prateleira_id || 'Indisponível'}</p>
            <p>Planta: ${semente}</p>
            <p><b>Status:</b> <i>${status}</i></p>
        `;
        
        container.appendChild(shelfCard);
    });
}

function isProducaoDisponivel(producao) {
    return producao && producao.dataInicio && producao.dataFim;
}

function calculateStatus(endDate) {
    const today = new Date();
    const end = new Date(endDate.split('T')[0]);
    return today <= end ? "Produzindo" : "Finalizado";
}

function calculateTotalDays(startDate, endDate) {
    const start = new Date(startDate.split('T')[0]);
    const end = new Date(endDate.split('T')[0]);
    const totalDays = Math.ceil((end - start) / (1000 * 60 * 60 * 24));
    return totalDays > 0 ? totalDays : 0;
}

function calculateDaysPassed(startDate) {
    const start = new Date(startDate.split('T')[0]);
    const today = new Date();
    const daysPassed = Math.ceil((today - start) / (1000 * 60 * 60 * 24));
    return daysPassed > 0 ? daysPassed : 0;
}

function calculateProgress(startDate, endDate) {
    const totalDays = calculateTotalDays(startDate, endDate);
    const daysPassed = calculateDaysPassed(startDate);
    return ((daysPassed / totalDays) * 100).toFixed(2); 
}