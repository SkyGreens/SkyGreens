package com.skygreen.SkyGreen.entities;

import java.time.LocalDateTime;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity(name = "pedidoCompra")
@Table(name = "pedidoCompra")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class PedidoCompraEntity {
    

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer pedidoCompraId;

    private LocalDateTime dataPedido;

    private int quantidade;

    @ManyToOne
    @JoinColumn(name = "semente_id")
    private SementeEntity semente;

    @ManyToOne
    @JoinColumn(name = "fornecedor_id")
    private FornecedorEntity fornecedor;
}
