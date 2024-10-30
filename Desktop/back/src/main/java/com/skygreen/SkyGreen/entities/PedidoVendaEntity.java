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

@Entity(name = "pedidoVenda")
@Table(name = "pedidoVenda")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class PedidoVendaEntity {
    

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer pedidoVendaId;

    private LocalDateTime dataPedido;

    private Integer tempoCultivo;

    private int quantidade;

    public boolean ativo;

    @ManyToOne
    @JoinColumn(name = "semente_id")
    private SementeEntity semente;

    @ManyToOne
    @JoinColumn(name = "cliente_id")
    private ClienteEntity cliente;
}
