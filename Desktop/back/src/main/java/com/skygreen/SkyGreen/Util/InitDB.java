package com.skygreen.SkyGreen.Util;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import com.skygreen.SkyGreen.Controller.AuthenticationController;
import com.skygreen.SkyGreen.DTO.RegisterDTO;
import com.skygreen.SkyGreen.entities.UsuarioRole;

@Component
public class InitDB implements CommandLineRunner {

    @Autowired
    AuthenticationController authenticationController;

    public void inserindoRegistro() {
        System.out.println("Inserindo registros");

        RegisterDTO data = new RegisterDTO("12345678909", "admin", UsuarioRole.ADMIN, "admin@skygreen.com", true,
                "Admin");
        authenticationController.register(data);

    }

    @Override
    public void run(String... args) throws Exception {
        inserindoRegistro();
    }

}
