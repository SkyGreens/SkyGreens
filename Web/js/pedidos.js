async function get_orders(token, url) { 
    try {
        const response = await fetch(url, {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${token}`,
                "Content-Type": "application/json"
            }
        });

        if (response.ok) {
            console.log("Consulta realizada com sucesso:", response.status);
            const data = await response.json(); 
            return data;
        } else {
            console.log("Falha na consulta:", response.status);
            return []; 
        }
    } catch (error) {
        console.error("Erro ao realizar a consulta:", error);
        return []; 
    }
}

async function gerarPedidos(token, url) {
    const pedidos = await get_orders(token, url);
    const orderContent = document.getElementById('orderContent');
    orderContent.innerHTML = ''; 

    if (pedidos.length === 0) {
        const noRecordsRow = document.createElement('div');
        noRecordsRow.classList.add('no-records');
        noRecordsRow.innerHTML = 'Nenhum pedido encontrado';
        orderContent.appendChild(noRecordsRow);
    } else {

            if (url.includes("venda")){
                pedidos.forEach(pedido => {
                    const orderDiv = document.createElement('div');
                    orderDiv.classList.add('order');
                    console.log(pedido)
        
                    orderDiv.innerHTML = `
                        <p><i>Pedido</i> ${pedido.pedidoVendaId || "Não disponível"}</p>
                        <p><strong>Quantidade:</strong> ${pedido.quantidade || "Não disponível"}</p>
                        <p><strong>Cliente:</strong> ${pedido.cliente ? pedido.cliente.razaoSocial : "Cliente não informado"}, <i>${pedido.cliente ? pedido.cliente.cnpj : "CNPJ não informado"}</i></p>
                        <p><strong>Data:</strong> ${pedido.dataPedido ? pedido.dataPedido.split('T')[0] : "Data não disponível"}</p>
                        <p><strong>Prazo de entrega:</strong> ${pedido.tempoCultivo}</p>
                    `;
        
                    orderContent.appendChild(orderDiv);
                });
            } else {

                pedidos.forEach(pedido => {
                    const orderDiv = document.createElement('div');
                    orderDiv.classList.add('order');
                    console.log(pedido)
        
                    orderDiv.innerHTML = `
                    <p><i>Pedido</i> ${pedido.pedidoCompraId}</p>
                    <p><strong>Quantidade:</strong> ${pedido.quantidade}</p>
                    <p><strong>Fornecedor:</strong> ${pedido.fornecedor.razaoSocial}, <i>${pedido.fornecedor.cnpj}</i></p>
                    <p><strong>Data:</strong> ${pedido.dataPedido.split('T')[0]}</p>
                `;
        
                    orderContent.appendChild(orderDiv);
                });

            }
      
        
    }
}