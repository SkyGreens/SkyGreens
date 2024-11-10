const url_get_proveedores = "http://localhost:8080/skygreen/fornecedor/";
const url_get_insumos = "http://localhost:8080/skygreen/sementes/";
const url_sale_orders = "http://localhost:8080/skygreen/vendas/";

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