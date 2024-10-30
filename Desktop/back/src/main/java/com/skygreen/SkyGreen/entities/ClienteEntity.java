package com.skygreen.SkyGreen.entities;

import java.io.Serializable;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Data
@Entity
@Table(name = "CLIENTE")
public class ClienteEntity implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer clienteId;
    private Boolean ativo;

    private String email;

    private String telefone;

    private String endereco;

    private String cidade;

    private String estado;

    private String pais;

    private String razaoSocial;
    private String cnpj;

}
