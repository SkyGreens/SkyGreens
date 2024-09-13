package com.skygreen.SkyGreen.entities;

import java.util.Collection;
import java.util.List;

import org.hibernate.validator.constraints.Length;
import org.hibernate.validator.constraints.br.CPF;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.Email;
import lombok.Data;


@Data
@Entity(name = "usuario ")
@Table(name = "usuario")
public class UsuarioEntity implements UserDetails {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String senha;
    private Boolean ativo;
    @Email
    private String email;

    private UsuarioRole role;

    @Length(max = 50, message = "Limite de 50 caracteres excedido")
    private String nome;
    @CPF
    private String cpf;

    public UsuarioEntity(String cpf, String senha, UsuarioRole role){
        this.cpf = cpf;
        this.senha = senha;
        this.role = role;
    }


    @Override
    public Collection<? extends GrantedAuthority> getAuthorities(){
       if(this.role == UsuarioRole.ADMIN) return List.of(new SimpleGrantedAuthority("ROLE_ADMIN"), new SimpleGrantedAuthority("ROLE_GERENTEPRODUCAO"), new SimpleGrantedAuthority("ROLE_ASSISTENTEADMINISTRATIVO"));
       else if(this.role == UsuarioRole.ASSISTENTEPRODUCAO) return List.of(new SimpleGrantedAuthority("ROLE_ASSISTENTEPRODUCAO"));
       else return List.of(new SimpleGrantedAuthority("ROLE_GERENTEPRODUCAO"));
    }

    @Override
    public String getUsername(){
        return cpf;
    }
    
    @Override
    public String getPassword() {
        return senha;
    }
    @Override
    public boolean isAccountNonExpired(){
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
     }
     
     @Override
     public boolean isEnabled() {
        return true;
     }
    
     @Override
     public boolean isAccountNonLocked() {
        return true;
     }


}
