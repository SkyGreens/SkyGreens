package com.skygreen.SkyGreen.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.skygreen.SkyGreen.entities.ProducaoEntity;

@Repository
public interface ProducaoRepository extends JpaRepository<ProducaoEntity, Integer> {
    
}
