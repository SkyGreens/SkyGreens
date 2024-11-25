package com.skygreen.SkyGreen.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.skygreen.SkyGreen.entities.PedidoCompraEntity;

@Repository
public interface PedidoCompraRepository extends JpaRepository<PedidoCompraEntity, Integer> {
    
}
