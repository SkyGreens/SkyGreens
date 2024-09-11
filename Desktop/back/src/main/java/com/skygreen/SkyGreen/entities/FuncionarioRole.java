package com.skygreen.SkyGreen.entities;

public enum FuncionarioRole {
    
    ADMIN("admin"),
    GERENTEPRODUCAO("gerenteProducao"),
    ASSISTENTEADMINISTRATIVO("assistenteAdministrativo");

    private String role;

    FuncionarioRole(String role){
        this.role = role;
    }

    public String getRole(){
        return role;
    }
}
