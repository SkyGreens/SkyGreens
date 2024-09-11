package com.skygreen.SkyGreen.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

import com.skygreen.SkyGreen.DTO.AuthenticationDTO;

import jakarta.validation.Valid;

@Controller
@RequestMapping("auth")
public class AuthenticationController {
    @PostMapping("/login")
    public ResponseEntity login (@RequestBody @Valid AuthenticationDTO data){

    var usernamePassword = new UsernamePasswordAuthenticationToken(data.cpf(), data.senha());


    }
}