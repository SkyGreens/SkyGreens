package com.skygreen.SkyGreen.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.skygreen.SkyGreen.entities.PedidoVendaEntity;

@Repository
public interface PedidoVendaRepository extends JpaRepository<PedidoVendaEntity, Integer> {
    
}
