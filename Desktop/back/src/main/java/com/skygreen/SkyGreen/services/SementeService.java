package com.skygreen.SkyGreen.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.repositories.SementeRepository;

import jakarta.persistence.EntityNotFoundException;

@Service
public class SementeService {
    
    @Autowired
    private SementeRepository repository;

    public List<SementeEntity> findAll(){
        return repository.findAll();
    }

    public SementeEntity getSementeById(Integer id) {
        return repository.findById(id)
        .orElseThrow(() -> new EntityNotFoundException("Semente não encontrada"));
    }

    public SementeEntity criarSemente(SementeEntity semente){
        return repository.save(semente);
    }
}
