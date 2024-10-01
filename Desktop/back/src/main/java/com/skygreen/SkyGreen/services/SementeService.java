package com.skygreen.SkyGreen.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.skygreen.SkyGreen.entities.FornecedorEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.repositories.FornecedorRepository;
import com.skygreen.SkyGreen.repositories.SementeRepository;

import jakarta.persistence.EntityNotFoundException;

@Service
public class SementeService {
    
    @Autowired
    private SementeRepository sementeRepository;

    @Autowired
    private FornecedorRepository fornecedorRepository;

    public List<SementeEntity> findAll(){
        return sementeRepository.findAll();
    }

    public SementeEntity getSementeById(Integer id) {
        return sementeRepository.findById(id)
        .orElseThrow(() -> new EntityNotFoundException("Semente não encontrada"));
    }

    public SementeEntity criarSemente(SementeEntity semente) {
        // Busca o fornecedor usando o ID contido no objeto semente
        FornecedorEntity fornecedor = fornecedorRepository.findById(semente.getFornecedor().getFornecedorId())
                .orElseThrow(() -> new EntityNotFoundException("Fornecedor não encontrado"));

        // Associa a semente ao fornecedor
        semente.setFornecedor(fornecedor);

        // Salva a semente com o fornecedor vinculado
        return sementeRepository.save(semente);
    }
}
