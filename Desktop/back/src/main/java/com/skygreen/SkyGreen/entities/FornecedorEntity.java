package com.skygreen.SkyGreen.entities;

import java.io.Serializable;

import org.hibernate.validator.constraints.Length;
import org.hibernate.validator.constraints.br.CNPJ;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.Email;
import lombok.Data;


@Data
@Entity
@Table(name = "FORNECEDOR")
public class FornecedorEntity implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private Boolean ativo;
    @Email
    private String email;

    private String telefone;

    private String endereco;

    private String cidade;

    private String estado;

    private String pais;

    private Integer inscricao_estadual;

    @Length(max = 50, message = "Limite de 50 caracteres excedido")
    private String razao_social;
    @CNPJ
    private String cnpj;

}
