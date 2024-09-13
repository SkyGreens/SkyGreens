package com.skygreen.SkyGreen.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

import com.skygreen.SkyGreen.DTO.AuthenticationDTO;
import com.skygreen.SkyGreen.DTO.RegisterDTO;
import com.skygreen.SkyGreen.entities.UsuarioEntity;
import com.skygreen.SkyGreen.repositories.UsuarioRepository;

import jakarta.validation.Valid;

@Controller
@RequestMapping("auth")
public class AuthenticationController {

    @Autowired
    private UsuarioRepository repository;

    @Autowired
    private AuthenticationManager authenticationManager;

    @PostMapping("/login")
    public ResponseEntity login(@RequestBody @Valid AuthenticationDTO data) {

        var usernamePassword = new UsernamePasswordAuthenticationToken(data.cpf(), data.senha());
        var auth = this.authenticationManager.authenticate(usernamePassword);

        return ResponseEntity.ok().build();
    }

    @PostMapping("/register")
    public ResponseEntity register(@RequestBody @Valid RegisterDTO data) {

        if (this.repository.findUsuarioByCpf(data.cpf()) != null)
            return ResponseEntity.badRequest().build();

        String encryptedPassword = new BCryptPasswordEncoder().encode(data.senha());

        UsuarioEntity newUsuario = new UsuarioEntity(data.cpf(), encryptedPassword, data.role(), data.nome(), data.ativo(), data.email());

        this.repository.save(newUsuario);

        return ResponseEntity.ok().build();
    }
}