package com.skygreen.SkyGreen.services.interfaces;

import java.util.List;

import com.skygreen.SkyGreen.entities.FornecedorEntity;

public interface IFornecedorService {

    List<FornecedorEntity> findAll();
 
    FornecedorEntity findById(Integer id);

    FornecedorEntity add(FornecedorEntity fornecedor);

    FornecedorEntity update(FornecedorEntity fornecedor);    
    
    void delete(Integer id);
}