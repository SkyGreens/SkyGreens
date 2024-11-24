document.addEventListener('DOMContentLoaded', () => {
    const menuContainer = document.getElementById('menu-container');
    fetch('menu.html')
        .then(response => response.text())
        .then(data => {
            menuContainer.innerHTML = data;
        })
        .catch(error => {
            console.error('Erro ao carregar o menu:', error);
        });
});

function toggleHamburgerMenu() {
    const menu = document.querySelector('.hamburger-menu-options');
    menu.classList.toggle('open');
}

function toggleProfileMenu() {
    let profileMenu = document.getElementById('profile');

    if (!profileMenu) {
        const nome = localStorage.getItem("nome")?.trim() || "Usuário";
        const email = localStorage.getItem("email")?.trim() || "Email não disponível";

        profileMenu = document.createElement('div');
        profileMenu.id = 'profile';
        profileMenu.classList.add('profile-menu', 'show'); 
        profileMenu.innerHTML = `
            <div class="profile-header">
                <p>Nome: ${nome}</p>
                <p>Email: ${email}</p>
            </div>
            <div class="profile-body">
                <button class="btlogout" onclick="logout()">Sair</button>
            </div>
        `;

        document.body.appendChild(profileMenu);
    }

    if (profileMenu.classList.contains('hidden')) {
        profileMenu.classList.remove('hidden');
        profileMenu.classList.add('show');
    } else {
        profileMenu.classList.remove('show');
        profileMenu.classList.add('hidden');
    }
}
function logout() {
    const confirmLogout = confirm("Tem certeza que deseja desconectar?");
    if (confirmLogout) {
        localStorage.removeItem("authToken");
        localStorage.removeItem("IDUser");
        localStorage.removeItem("nome");
        localStorage.removeItem("email");
        window.location.href = "login.html"; 
    }
}