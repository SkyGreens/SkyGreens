package com.skygreen.SkyGreen.entities;

import java.util.ArrayList;
import java.util.List;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity(name = "semente")
@Table(name = "semente")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class SementeEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer sementeId;

    private String nome;
    private String descricao;

    @ManyToOne
    @JoinColumn(name = "fornecedor_id")
    private FornecedorEntity fornecedor;

    @OneToOne(mappedBy = "semente", cascade = CascadeType.ALL)
    private EstoqueEntity estoque;

    @OneToMany(mappedBy = "semente", cascade = CascadeType.ALL)
    private List<PedidoCompraEntity> pedidosCompra = new ArrayList<>();

    
    
}
