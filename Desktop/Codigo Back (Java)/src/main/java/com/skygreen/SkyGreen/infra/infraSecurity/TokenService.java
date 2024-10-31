package com.skygreen.SkyGreen.infra.infraSecurity;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.lang.RuntimeException;
import java.time.ZoneOffset;
import java.time.LocalDateTime;
import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTCreationException;
import com.auth0.jwt.exceptions.JWTVerificationException;
import com.skygreen.SkyGreen.entities.UsuarioEntity;

@Service
public class TokenService {
    
    @Value("${api.security.token.secret}")

    private String secret;
    
    public String generatedToken (UsuarioEntity usuario){

        try{
            Algorithm algorithm = Algorithm.HMAC256(secret);
            String token= JWT.create()
            .withIssuer("auth-api")
            .withSubject(usuario.getCpf())
            .withExpiresAt(genExpirationDate())
            .sign(algorithm);

            return token;
        }catch(JWTCreationException exception){
            throw new RuntimeException("Error while generating token", exception);
        }
    }

    public String validadeToken(String token){

        try{
            Algorithm algorithm = Algorithm.HMAC256(secret);
            return JWT.require(algorithm)
            .withIssuer("auth-api")
            .build()
            .verify(token)
            .getSubject();
        }catch(JWTVerificationException e ){
            return "";
        }
    }

    private Instant genExpirationDate(){
        return LocalDateTime.now().plusHours(2).toInstant(ZoneOffset.of("-03:00"));
    }
}
