package com.skygreen.SkyGreen.services.interfaces;

import java.util.List;
import java.util.Optional;

import com.skygreen.SkyGreen.entities.ProducaoEntity;

public interface IProducaoService {

    List<ProducaoEntity> findAll();
 
    Optional<ProducaoEntity> findById(Integer id);

    ProducaoEntity add(ProducaoEntity producao) throws Exception;

    ProducaoEntity update(ProducaoEntity producao) throws Exception;    
    
    void delete(Integer id);

}