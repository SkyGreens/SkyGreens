package com.skygreen.SkyGreen.entities;

import java.io.Serializable;

import org.hibernate.validator.constraints.Length;
import org.hibernate.validator.constraints.br.CPF;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.Email;
import lombok.Data;


@Data
@Entity
@Table(name = "FUNCIONARIO")
public class FuncionarioEntity implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    @Length(max = 30, message = "Limite de 30 caracteres excedido")
    private String senha;
    private Boolean ativo;
    @Email
    private String email;

    private Integer cargo_id;

    @Length(max = 50, message = "Limite de 50 caracteres excedido")
    private String nome;
    @CPF
    private String cpf;
    


}
