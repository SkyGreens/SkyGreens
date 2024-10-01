package com.skygreen.SkyGreen.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;
import com.skygreen.SkyGreen.entities.FornecedorEntity;
import com.skygreen.SkyGreen.repositories.FornecedorRepository;
import com.skygreen.SkyGreen.services.interfaces.IFornecedorService;

import jakarta.persistence.EntityNotFoundException;

@Service
public class FornecedorServiceImpl implements IFornecedorService {

    @Autowired
    private FornecedorRepository repository;
    
    @Override
    public List<FornecedorEntity> findAll(){
        return repository.findAll();
    }

    @Override
    public FornecedorEntity add(FornecedorEntity fornecedor){
        fornecedor = repository.save(fornecedor);
        return fornecedor;
    }

    @Override
    public Optional<FornecedorEntity> findById(Integer id){
       return repository.findById(id);
    }

    @Override
    public void delete(Integer id){
        repository.deleteById(id);
    }

    @Override
    public FornecedorEntity update(@RequestBody FornecedorEntity fornecedor){       
        fornecedor = repository.save(fornecedor);
        return fornecedor;
    }


}
