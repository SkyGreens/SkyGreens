function show_orders(){
    window.location.href = "pedidos.html";
}

function show_proveedores(){
    window.location.href = "listaFornecedores.html";
}

function homepage(){
    window.location.href = "home.html";
}

function pageInsumo(){
    window.location.href = "insumo.html";
}

function userpage(){
    window.location.href = "usuarios.html";
}

function show_production(){
    window.location.href = "producao.html";
}

function monitoring_page(){
    window.location.href = "monitoramento.html";
}

function report_page(){
    window.location.href = "relatorio.html";
}

function sales_page(){
    window.location.href = "pedido_venda.html";
}

function purchase_page(){
    window.location.href = "pedido_compra.html";
}

function stock_page(){
    window.location.href = "estoque.html";
}

function logout(){
    const userConfirmed = confirm('Tem certeza que deseja desconectar?');
    
    if (userConfirmed) {
        window.location.href = "login.html";
    } 
    
}

//TODO: não tenho a api ainda
const url_get_orders = "http://localhost:8080/skygreen/pedido/";

async function get_orders(token) { 

    getData = {
        token: token
    };

    try {
        const response = await fetch(url_get_orders, {
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

async function gerarPedidos() { //parametro = response da func de cima

    const pedidos = await get_orders(token);
    const orderContent = document.getElementById('orderContent');
    orderContent.innerHTML = ''; 

    if (pedidos.length === 0) {
        const noRecordsRow = document.createElement('div');
        noRecordsRow.classList.add('no-records');
        noRecordsRow.innerHTML = 'Nenhum pedido encontrado';
        orderContent.appendChild(noRecordsRow);
    } else {

        pedidos.forEach(pedido => {
            const orderDiv = document.createElement('div');
            orderDiv.classList.add('order');

            orderDiv.innerHTML = `
                <p><i>Pedido</i> ${pedido.id}</p>
                <p><strong>Cliente:</strong> ${pedido.cliente}</p>
                <p><strong>Produto:</strong> ${pedido.produto}</p>
                <p><strong><i>Prazo de Entrega</i></strong> ${pedido.prazo}</p>
            `;

            orderContent.appendChild(orderDiv);
        });
    } 
}

// function login_submit(){

//     document.getElementById("loginForm").addEventListener("submit", function(event) {
//         event.preventDefault();
    
//         var user = document.getElementById("user").value;
//         var password = document.getElementById("password").value;

//         do_login(user, password).then(success => {
//             if (success) {
//                 alert("Login realizado com sucesso!"); 
//                 console.log("Login realizado com sucesso!");
//                 homepage(); 
//             } else {
//                 console.log("Login falhou.");
//                 alert("Usuário ou senha inválida. Por favor, tente novamente."); 
//             }
//         });

//     });

// }

// function forgotPassword() {

//     const email = prompt("Por favor, insira seu e-mail para recuperar a senha:");

//     if (email) {
//         alert(`Um link de recuperação de senha foi enviado para: ${email}`);
//     } else {
//         alert("Você precisa inserir um e-mail válido para recuperar a senha.");
//     }
// }

// const urlLogin = "http://localhost:8080/skygreen/auth/login";
// let token = null;

// async function do_login(cpf, senha) {

//     loginData = {
//         cpf: cpf, 
//         senha: senha
//     };

//     try {
//         const response = await fetch(urlLogin, {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify(loginData)
//         });

//         const data = await response.json();
//         token = data.token;

//         if (response.ok) {
//             console.log("Login realizado com sucesso:", response.status);
//             return { success: true, token: token };
//         } else {
//             console.log("Falha no login:", response.status);
//             return { success: false, token: null };
//         }
//     } catch (error) {
//         console.error("Erro ao realizar o login:", error);
//         return { success: false, token: null };
//     }
// }

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

/*
document.addEventListener('DOMContentLoaded', function() {
    fetchSuppliers(token);
});

async function get_proveedores(token) { 
    console.log(token);

    try {
        const response = await fetch("http://localhost:8080/skygreen/fornecedor/", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}` 
            }
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Consulta realizada com sucesso:", response.status);
            return data; 
        } else {
            console.log("Falha na consulta:", response.status);
            return null;
        }
    } catch (error) {
        console.error("Erro ao realizar a consulta:", error);
        return null;
    }
}
    

async function fetchSuppliers(token) { 
    const suppliers = await get_proveedores(token);

    if (suppliers && Array.isArray(suppliers)) { 
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
        console.error('Erro ao buscar fornecedores: Nenhum fornecedor encontrado.');
    }
}*/

// function inactivateUser(button) {
//     const userCard = button.parentElement; 
//     const statusElement = userCard.querySelector(".user-status"); 

//     if (statusElement.textContent === "Ativo") {

//         const confirmInactivate = confirm("Você tem certeza que deseja inativar este usuário?");
        
//         if (confirmInactivate) {
//             statusElement.textContent = "Inativo"; 
//             button.textContent = "Reativar Usuário"; 
//         }
//     } else {
        
//         const confirmReactivate = confirm("Você tem certeza que deseja reativar este usuário?");
        
//         if (confirmReactivate) {
//             statusElement.textContent = "Ativo"; 
//             button.textContent = "Inativar Usuário"; 
//         }
//     }
// }

function toggleProfileMenu() {
    var menu = document.getElementById("profileMenu");
    menu.classList.toggle("show");
}

document.querySelector('.profile-icon-container').addEventListener('click', function () {
    document.querySelector('.profile-menu').classList.toggle('show');
});

// Fechar o menu se clicar fora dele
window.onclick = function(event) {
    var menu = document.getElementById("profileMenu");
    if (!event.target.matches('.profile-icon') && !event.target.matches('.profile-icon-container')) {
        if (menu.classList.contains('show')) {
            menu.classList.remove('show');
        }
    }
}

// document.addEventListener("DOMContentLoaded", function() {
//     const iframe = document.getElementById("fornecedores-iframe");

//     iframe.onload = function() {
//         try {
//             getFornecedoresFromTable();
//         } catch (error) {
//             console.error("Erro ao acessar o conteúdo do iframe:", error);
//         }
//     };
// });

// function getFornecedoresFromTable() {
//     const iframe = document.getElementById("fornecedores-iframe");
//     const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;

//     if (!iframeDoc) {
//         console.error("O documento do iframe não está acessível.");
//         return;
//     }

//     const table = iframeDoc.getElementById("supplierTable");

//     if (!table) {
//         console.error("A tabela de fornecedores não foi encontrada no iframe.");
//         return;
//     }

//     const fornecedoresList = document.getElementById("fornecedores-list");
//     const rows = table.querySelectorAll("tbody tr");

//     fornecedoresList.innerHTML = "";

//     rows.forEach(row => {
//         const nome = row.cells[0].textContent;

//         const listItem = document.createElement("li");
//         listItem.innerHTML = `<strong>${nome}</strong><br>`;
//         fornecedoresList.appendChild(listItem);
//     });
// }