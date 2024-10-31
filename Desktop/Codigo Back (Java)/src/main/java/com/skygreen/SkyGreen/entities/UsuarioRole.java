package com.skygreen.SkyGreen.entities;

public enum UsuarioRole {
    
    ADMIN("admin"),
    GERENTEPRODUCAO("gerenteProducao"),
    ASSISTENTEPRODUCAO("assistenteProducao");

    private String role;

    UsuarioRole(String role){
        this.role = role;
    }

    public String getRole(){
        return role;
    }
}
