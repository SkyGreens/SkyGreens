package com.skygreen.SkyGreen.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.skygreen.SkyGreen.entities.PedidoCompraEntity;

public interface PedidoCompraRepository extends JpaRepository<PedidoCompraEntity, Integer> {
    
}
