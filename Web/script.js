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

// FAZER LOGIN URL
const urlLogin = "http://localhost:8080/skygreen/auth/login";
// CONSULTA ESTOQUE URL
const url_get_stocks = "http://localhost:8080/skygreen/estoque/";
// CONSULTA FORNECEDOR URL
const url_get_proveedores = "http://localhost:8080/skygreen/fornecedor/";
// CONSULTA INSUMOS URL
const url_get_insumos = "http://localhost:8080/skygreen/sementes/";
// CONSULTA PEDIDOS VENDA URL
const url_sale_orders = "http://localhost:8080/skygreen/vendas/";
// CONSULTA PEDIDO DE VENDA URL
const url_buy_orders = "http://localhost:8080/skygreen/compras/";
// CONSULTA PRODUÇÃO URL
const url_get_production = "http://localhost:8080/skygreen/producao/";
// CONSULTA PRATELEIRAS MONITORAMENTO URL
const url_get_shelves = "http://localhost:8080/skygreen/prateleira/";
// CONSULTA USUARIOS DO SISTEMA URL
const url_get_users = "http://localhost:8080/skygreen/usuario/";
// CONSULTA PERFIL URL
const url_profile = "http://localhost:8080/skygreen/usuario/personal/";
