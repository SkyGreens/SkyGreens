package com.skygreen.SkyGreen.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.skygreen.SkyGreen.entities.EstoqueEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;
import java.util.List;


@Repository
public interface EstoqueRepository extends JpaRepository<EstoqueEntity, Integer>{
    List<EstoqueEntity> findBySemente(SementeEntity semente);
}
