async function productionRequest(token){
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
        return productionData;

    } catch (error) {
        console.error("Erro ao carregar dados de produção:", error);
        return null;
    }     
}

async function renderProductionReports(token) {
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

        const reportContainer = document.querySelector('.report-item-container');
        reportContainer.innerHTML = ''; 

        productionData.forEach(report => {
            const reportCard = document.createElement('div');
            reportCard.classList.add('report-item');

            const dateNow = calcularDiasRestantes(report.dataFim.split('T')[0], report.tempoCultivo)
            
            reportCard.innerHTML = `
                <div class="report-header">
                    <div><span>Código do item: ${report.producaoId || 'Não disponível'}</span></div>
                    <div>Data: ${report.dataInicio.split('T')[0] || 'Não disponível'}</div>
                </div>
                <div class="report-body">
                    <div class="report-data">
                        <strong>Produto:</strong> ${report.sementeId || 'Não disponível'}
                    </div>
                    <div class="report-data">
                        <strong>Quantidade:</strong> <span class="data-box">${report.sementeQuantidade || 'Não disponível'}</span>
                    </div>
                    <div class="report-data">
                        <strong>Tempo de Cultivo:</strong> <span class="data-box">${report.tempoCultivo || 'Não disponível'}</span>
                    </div>
                    <div class="report-data">
                        <strong>Restam:</strong> <span class="data-box">${dateNow || 'Não disponível'}</span> 
                    </div>
                </div>
            `;

            reportContainer.appendChild(reportCard);
            return productionData;
        });
    } catch (error) {
        console.error("Erro ao carregar dados de produção:", error);
    }
}

function calcularDiasRestantes(datafim, tempocultivo) {
    const hoje = new Date();  
    const fim = new Date(datafim);

    if (hoje >= fim) {
        return 0;
    }

    const diferencaEmMilissegundos = fim - hoje;
    const diasRestantes = Math.ceil(diferencaEmMilissegundos / (1000 * 60 * 60 * 24)); 

    return Math.min(diasRestantes, tempocultivo); 
}

async function gerarCsv() {

    const token = localStorage.getItem("authToken")?.trim();
    const dados = await productionRequest(token); 
    console.log(dados);

    let csvContent = "data:text/csv;charset=utf-8,";
    csvContent += "Código do Item, Data, Produto, Quantidade, Tempo de Cultivo\n";

    dados.forEach(item => {
        const row = [
            item.producaoId,
            item.dataInicio.split('T')[0],
            item.sementeId,
            item.sementeQuantidade,
            item.tempoCultivo
        ].join(","); 
        csvContent += row + "\n"; 
    });

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "dados_producao.csv");
    document.body.appendChild(link);

    link.click(); 
    document.body.removeChild(link); 
}

