function forgotPassword() {
    alert("Contate o administrador do sistema para recuperar a senha.");
}

async function do_login(cpf, senha) {
    const loginData = { cpf: cpf, senha: senha };

    try {
        const response = await fetch(urlLogin, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(loginData)
        });

        const responseJson = await response.json();
        const token = responseJson.token;
        const user = responseJson.userId;

        if (response.ok) { 
            console.log("Login realizado com sucesso:", response.status);
            localStorage.setItem("authToken", token);
            localStorage.setItem("IDUser", user); 
            getProfile()
            return { success: true, token: token };
        } else {
            console.log("Falha no login:", response.status);
            return { success: false, token: null };
        }
    } catch (error) {
        console.error("Erro ao realizar o login:", error);
        return { success: false, token: null };
    }
}

function login_submit() {
    document.getElementById("loginForm").addEventListener("submit", function(event) {
        event.preventDefault();
    
        var user = document.getElementById("user").value;
        var password = document.getElementById("password").value;

        do_login(user, password).then(response => {
            if (response.success) {
                alert("Login realizado com sucesso!"); 
                console.log("Login realizado com sucesso!");
                homepage(); 
            } else {
                console.log("Login falhou.");
                alert("Usuário ou senha inválida. Por favor, tente novamente."); 
            }
        });
    });
}

async function getProfile() {
    const token = localStorage.getItem("authToken")?.trim();
    const IDUser = localStorage.getItem("IDUser")?.trim();

    try {
        const response = await fetch(url_profile + IDUser, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }

        const usuario = await response.json();
        const nome = usuario.nome;
        const email = usuario.email;
        localStorage.setItem("nome", nome);
        localStorage.setItem("email", email);

        return usuario || {};
    } catch (error) {
        console.error('Erro ao buscar usuário:', error);
        return null;
    }
}