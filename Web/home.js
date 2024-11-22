async function renderFromStorage(token) {
    try {
        const fornecedores = await getFornecedor(token);
        const insumos = await getInsumos(token);
        const pedidos = await getOrders(token); 

        const fornecedoresInfoCard = document.getElementById('fornecedores-info-card');

        if (fornecedoresInfoCard && Array.isArray(fornecedores)) { 
            fornecedores.forEach(fornecedor => {
                const divFornecedor = document.createElement('li');
                divFornecedor.textContent = fornecedor.razaoSocial;  
                fornecedoresInfoCard.appendChild(divFornecedor);
            });
        } else {
            console.error("Elemento fornecedores-list não encontrado.");
        }

        const insumosList = document.getElementById('sementes-info-card');
        if (insumosList) { 
            insumos.forEach(insumo => {
                const li = document.createElement('li');
                li.textContent = insumo.nome;
                insumosList.appendChild(li);
            });
        } else {
            console.error("Elemento sementes-list não encontrado.");
        }

        const pedidosTable = document.getElementById('pedido-info-card');
        if (pedidosTable) {
            pedidos.forEach(pedido => {
                const tr = document.createElement('tr');
                tr.innerHTML = `<td>#${pedido.pedidoVendaId} - ${pedido.semente.nome}</td>`;
                pedidosTable.appendChild(tr);
            });
        } else {
            console.error("Elemento da tabela de pedidos não encontrado.");
        }
    } catch (error) {
        console.error("Erro ao carregar dados:", error);
    }
}

async function getOrders(token) {
    try {
        const response = await fetch(url_sale_orders, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }

        const pedidos = await response.json();
        return pedidos || [];
    } catch (error) {
        console.error('Erro ao buscar pedidos:', error);
        return []; 
    }
}


async function getFornecedor(token) {
    try {
        const response = await fetch(url_get_proveedores, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }
        const data = await response.json();
        return data || []; 
    } catch (error) {
        console.error("Erro ao obter fornecedores:", error);
        return []; 
    }
}

async function getInsumos(token) {
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
        return insumos || [];
    } catch (error) {
        console.error('Erro ao buscar insumos:', error);
        return [];
    }
}

async function getStock(token) {
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

        const stock = await response.json();
        return stock || [];
    } catch (error) {
        console.error('Erro ao buscar estoque:', error);
        return [];
    }
}

async function getProducao(token) {
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

        const stock = await response.json();
        return stock || [];
    } catch (error) {
        console.error('Erro ao buscar estoque:', error);
        return [];
    }
}

async function fetchCharts(token) {
    try {

        estoque(token);
        producaoGeral(token);

    } catch (error) {
        console.error('Erro ao buscar dados da API:', error);
    }
}

async function producaoGeral(token) {
    const pedidosData = await getOrders(token);
    const estoqueData = await getStock(token);
    const producaoData = await getProducao(token);

    if (!pedidosData || !estoqueData || !producaoData) {
        throw new Error('Um ou mais dados necessários não foram retornados.');
    }

    console.log('Dados Gerais:', { pedidosData, estoqueData, producaoData });

    const chart2Container = document.querySelector('[data-chart-id="chart2"]');
    const chart2 = chart2Container.querySelector('.chart');
    chart2Container.querySelectorAll('.label').forEach(label => label.remove());

    const pedidosQuantidade = pedidosData.reduce((total, item) => total + (item.quantidade || 0), 0);
    const estoqueQuantidade = estoqueData.reduce((total, item) => total + (item.quantidade || 0), 0);
    const producaoQuantidade = producaoData.reduce((total, item) => total + (item.sementeQuantidade || 0), 0);

    const categorias = [
        { nome: 'Pedidos', quantidade: pedidosQuantidade },
        { nome: 'Estoque', quantidade: estoqueQuantidade },
        { nome: 'Produção', quantidade: producaoQuantidade }
    ];

    const total = categorias.reduce((sum, categoria) => sum + categoria.quantidade, 0);

    const fixedColors = ['#304019', '#495c2e', '#b8bbb4'];

    let offset = 0; 
    categorias.forEach((item, index) => {
        const percentage = (item.quantidade / total) * 100;
        const angle = (percentage / 100) * 360; 

        const label = document.createElement('span');
        label.classList.add('label');
        label.textContent = `${item.nome}: ${percentage.toFixed(2)}%`;

        label.style.color = 'black';

        const centerX = 40; 
        const centerY = 50; 
        const radius = 45; 

        const labelAngle = (offset + (angle / 2)) * (Math.PI / 180); 

        let labelX = centerX + radius * Math.cos(labelAngle);
        let labelY = centerY + radius * Math.sin(labelAngle);

        // if (item.nome === 'Pedidos') {
        //     label.style.top = `calc(${labelY}% - 215px)`; 
        //     label.style.textAlign = 'center';
        //     label.style.position = 'center';
        // }

        if (item.nome === 'Estoque') {
            label.style.top = `calc(${labelY}% - 300px)`; 
            label.style.left = `calc(${labelX}% - 90px)`; 
            label.style.position = 'center';
        }

        if (item.nome === 'Produção') {
            label.style.right = `calc(${labelX}% - 320px)`; 
            label.style.top = `calc(${labelY}% - 230px)`; 
        }

        chart2Container.appendChild(label);

        offset += angle; 
    });

    renderChart2(chart2, categorias, total);
}

async function renderChart2(chartElement, categorias, total) {
    let gradientParts = [];
    let offset = 0;

    categorias.forEach((item, index) => {
        const percentage = (item.quantidade / total) * 100;
        const color = index === 0 ? '#304019' : index === 1 ? '#495c2e' : '#b8bbb4';

        gradientParts.push(`${color} ${offset}% ${offset + percentage}%`);
        offset += percentage;
    });

    const gradient = gradientParts.join(', ');

    chartElement.style.background = `conic-gradient(${gradient})`;
}

async function estoque(token) {
    const stockData = await getStock(token);

    if (!stockData || stockData.length === 0) {
        throw new Error('Nenhum dado de estoque foi retornado.');
    }

    console.log('Dados do estoque:', stockData);

    const chart1Container = document.querySelector('[data-chart-id="chart1"]');
    const chart1 = chart1Container.querySelector('.chart');
    chart1Container.querySelectorAll('.label').forEach(label => label.remove());

    const totalStock = stockData.reduce((total, item) => total + item.quantidade, 0);

    let offset = 0;
    const fixedColors = ['#495c2e', '#4a90e2', '#e94e77']; 

    stockData.forEach((item, index) => {
        const percentage = (item.quantidade / totalStock) * 100;
        const color = fixedColors[index % fixedColors.length];

        chart1.style.setProperty(`--value-${index}`, `${percentage.toFixed(1)}%`);
        chart1.style.setProperty(`--color-${index}`, color);

        const label = document.createElement('span');
        label.classList.add('label'); 
        label.style.color = 'black';
        label.textContent = `${item.semente.nome}: ${percentage.toFixed(2)}%`;

        chart1Container.appendChild(label);

        offset += percentage;
    });

    renderChart1(chart1, stockData, totalStock);
}

async function renderChart1(chartElement, stockData, totalStock) {
    let gradientParts = [];
    let offset = 0;
    const fixedColors = ['#495c2e', '#4a90e2', '#e94e77']; 

    stockData.forEach((item, index) => {
        const percentage = (item.quantidade / totalStock) * 100;
        const color = fixedColors[index % fixedColors.length]; 
        gradientParts.push(`${color} ${offset}% ${offset + percentage}%`);
        offset += percentage;
    });

    const gradient = gradientParts.join(', ');

    chartElement.style.setProperty('--colors', gradient);
}