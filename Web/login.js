function forgotPassword() {
    alert("Contate o administrador do sistema para recuperar a senha.");
}

function homepage(){
    window.location.href = "home.html";
}

const urlLogin = "http://localhost:8080/skygreen/auth/login";

// async function do_login(cpf, senha) {

//     const loginData = {
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

//         const token = await response.text();

//         if (response.ok) { // 200 OK
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

        if (response.ok) { // 200 OK
            console.log("Login realizado com sucesso:", response.status);
            localStorage.setItem("authToken", token);
            localStorage.setItem("IDUser", user);
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