package com.skygreen.SkyGreen.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.skygreen.SkyGreen.entities.SementeEntity;

@Repository
public interface SementeRepository extends JpaRepository<SementeEntity, Integer>{
    
}
