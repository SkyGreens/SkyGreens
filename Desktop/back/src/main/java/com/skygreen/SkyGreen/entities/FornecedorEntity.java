package com.skygreen.SkyGreen.entities;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import org.hibernate.validator.constraints.Length;
import org.hibernate.validator.constraints.br.CNPJ;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonManagedReference;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
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
    private Integer fornecedorId;
    private Boolean ativo;

    private String email;

    private String telefone;

    private String endereco;

    private String cidade;

    private String estado;

    private String pais;

    private Integer inscricaoEstadual;

    private String razaoSocial;
    private String cnpj;

    @OneToMany(mappedBy = "fornecedor", cascade = CascadeType.ALL)
    @JsonManagedReference
    private List<SementeEntity> sementes = new ArrayList<>();

}
