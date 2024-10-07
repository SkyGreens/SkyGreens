package com.skygreen.SkyGreen.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.skygreen.SkyGreen.entities.EstoqueEntity;

public interface EstoqueRepository extends JpaRepository<EstoqueEntity, Integer>{
    
}
