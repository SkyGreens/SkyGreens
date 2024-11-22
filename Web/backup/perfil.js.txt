const url_profile = "http://localhost:8080/skygreen/usuario/personal/";

// async function fetchProfile(){

//     const token = localStorage.getItem("authToken")?.trim();
//     const user = localStorage.getItem("IDUser")?.trim();

//     try {
//         const response = await fetch(url_profile + user, { 
//             method: 'GET',
//             headers: {
//                 'Authorization': `Bearer ${token}`,
//                 'Content-Type': 'application/json'
//             }
//         });

//         if (!response.ok) {
//             throw new Error(`Erro na requisição: ${response.status}`);
//         }

//         const users = await response.json();
//         const profile = document.querySelector('profileMenu');
//         profile.innerHTML = ''; 

//         users.forEach(user => {
//             const userCard = document.createElement('div');
      
//             userCard.innerHTML = `
//                 <div class="report-body">
//                     <p><strong>Usuário:</strong> ${user.nome || 'Não disponível'}</p>
//                     <p><strong>Email:</strong> ${user.email || 'Não disponível'}</p>
//                     <button class="btlogout" onclick="logout()">Logout</button>
//                 </div>
//             `;
        
//             document.getElementById('profileMenu').appendChild(userCard);
//             return users;
//         });
//     } catch (error) {
//         console.error('Erro ao buscar usuários:', error);
//     }

// }

async function loadProfileMenu() {
    const response = await fetch('perfil.html');
    const menuHTML = await response.text();
    document.body.insertAdjacentHTML('beforeend', menuHTML);
}

function toggleProfileMenu() {
    const profileMenu = document.getElementById('profileMenu');
    console.log(profileMenu);
    if (profileMenu) {
        profileMenu.classList.toggle('hidden');
    }
}

// Carregar o menu assim que o arquivo for carregado
window.addEventListener('DOMContentLoaded', loadProfileMenu);