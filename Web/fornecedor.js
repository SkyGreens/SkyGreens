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
    try {
        const response = await fetch(url_get_proveedores, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Erro ao realizar a consulta:', error);
        return null;
    }
}

async function fetchSuppliers(token) { 
    try {
        const suppliers = await get_proveedores(token);
        console.log(suppliers);

        if (suppliers) {
            const tableBody = document.getElementById('tableBody');

            tableBody.innerHTML = '';

            suppliers.forEach(supplier => {
                const row = document.createElement('tr');
                
                const status = supplier.ativo ? "ativo" : "inativo";
                row.setAttribute("data-status", status);
                
                row.innerHTML = `
                    <td>${supplier.razaoSocial}</td>
                    <td>${supplier.email}</td>
                    <td>${supplier.inscricaoEstadual}</td>
                    <td>${supplier.cnpj}</td>
                    <td>${supplier.pais}</td>
                    <td>${supplier.telefone}</td>
                    <td>${supplier.cidade}</td>
                    <td>${supplier.estado}</td>
                    <td class="status">${supplier.ativo ? "Ativo" : "Inativo"}</td>
                `;

                tableBody.appendChild(row);
            });
        } else {
            console.error('Erro ao buscar fornecedores.');
        }
    } catch (error) {
        console.error('Erro ao realizar a consulta:', error);
    }
}