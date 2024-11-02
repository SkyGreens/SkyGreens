function show_proveedores(){
    window.location.href = "listaFornecedores.html";
}

function filterTable() {
    const filter = document.getElementById("statusFilter").value;
    const rows = document.querySelectorAll("#supplierTable tbody tr");

    rows.forEach(row => {
        const status = row.getAttribute("data-status");

        if (filter === "all" || status === filter) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}

document.getElementById("searchBar").addEventListener("keyup", function () {
    const searchText = this.value.toLowerCase();
    const rows = document.querySelectorAll("#supplierTable tbody tr");

    rows.forEach(row => {
        const name = row.cells[0].innerText.toLowerCase();
        if (name.includes(searchText)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
});

const url_get_proveedores = "http://localhost:8080/skygreen/fornecedor/";

async function get_proveedores(token) { 

    getData = {
        token: token
    };

    try {
        const response = await fetch(url_get_proveedores, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(getData)
        });

        if (response.ok) {
            console.log("Consulta realizada com sucesso:", response.status);
            return response;
        } else {
            console.log("Falha na consulta:", response.status);
            return response;
        }
    } catch (error) {
        console.error("Erro ao realizar a consulta:", error);
        return response;
    }
}

async function fetchSuppliers(token) { 
    const suppliers = await get_proveedores(token);

    if (suppliers) {
        const tableBody = document.getElementById('tableBody');

        tableBody.innerHTML = '';

        suppliers.forEach(supplier => {
            const row = document.createElement('tr');
            
            row.innerHTML = `
                <td>${supplier.nome}</td>
                <td>${supplier.email}</td>
                <td>${supplier.inscricao_estadual}</td>
                <td>${supplier.cnpj}</td>
                <td>${supplier.pais}</td>
                <td>${supplier.telefone}</td>
                <td>${supplier.cidade}</td>
                <td>${supplier.estado}</td>
                <td class="status">${supplier.status}</td>
            `;

            tableBody.appendChild(row);
        });
    } else {
        console.error('Erro ao buscar fornecedores:', error);
    }
}
