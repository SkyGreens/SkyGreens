const url_get_users = "http://localhost:8080/skygreen/usuario/";

async function fetchUsers(token) {
    try {
        const response = await fetch(url_get_users, { 
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }

        const users = await response.json();
        renderUsers(users);
    } catch (error) {
        console.error('Erro ao buscar usuários:', error);
    }
}

function renderUsers(users) {
    const cardContainer = document.querySelector('.card-container');
    cardContainer.innerHTML = '';  

    users.forEach(user => {
        const userCard = document.createElement('div');
        userCard.classList.add('user-card');
        userCard.innerHTML = `
            <h3>${user.nome}</h3>
            <p><i>${user.role}</i></p>
            <div class="user-details">
                <p>Status: <span class="user-status">${user.ativo}</span></p>
                <p>Usuário: ${user.username}</p>
                <p>Email:${user.email}</p>
                <p>Senha: ********</p>
            </div>
        `;
        cardContainer.appendChild(userCard);
    });
}


