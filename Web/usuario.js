const url_get_users = "http://localhost:8080/skygreen/usuario/";
const url_profile = "http://localhost:8080/skygreen/usuario/personal/";

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
            <img src="${user.profilePic}" alt="Foto de perfil" class="profile-pic">
            <h3>${user.nome}</h3>
            <p><i>${user.role}</i></p>
            <div class="user-details">
                <p>Status: <span class="user-status">${user.ativo}</span></p>
                <p>Usuário: ${user.username}</p>
                <p>Email: ${user.email}</p>
                <p>Senha: ********</p>
            </div>
        `;
        cardContainer.appendChild(userCard);
    });
}

async function teste(){

    const token = localStorage.getItem("authToken")?.trim();

    try {
        const response = await fetch(url_profile, { 
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
        const profile = document.querySelector('profileMenu');
        profile.innerHTML = ''; 

        users.forEach(user => {
            const userCard = document.createElement('div');
      
            userCard.innerHTML = `
                <div class="report-body">
                    <p><strong>Usuário:</strong> ${user.nome || 'Não disponível'}</p>
                    <p><strong>Email:</strong> ${user.email || 'Não disponível'}</p>
                    <button class="btlogout" onclick="logout()">Logout</button>
                </div>
            `;
        
            // Adiciona o cartão ao container desejado (substitua 'containerElement' pelo id ou classe do elemento onde você deseja colocar os cards)
            document.getElementById('profileMenu').appendChild(userCard);
            return users;
        });
    } catch (error) {
        console.error('Erro ao buscar usuários:', error);
    }

}
