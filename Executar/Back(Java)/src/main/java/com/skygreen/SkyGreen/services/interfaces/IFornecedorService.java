package com.skygreen.SkyGreen.services.interfaces;

import java.util.List;
import java.util.Optional;

import com.skygreen.SkyGreen.entities.FornecedorEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;

public interface IFornecedorService {

    List<FornecedorEntity> findAll();
 
    Optional<FornecedorEntity> findById(Integer id);

    FornecedorEntity add(FornecedorEntity fornecedor);

    FornecedorEntity update(FornecedorEntity fornecedor);    
    
    FornecedorEntity updateSementes(Integer fornecedorId, List<SementeEntity> sementes);
    
    void delete(Integer id);

    List<SementeEntity> buscarSementePorFornecedor(int forncedorId);

    FornecedorEntity removeSementeFromFornecedor(Integer fornecedorId, Integer sementeId);

}