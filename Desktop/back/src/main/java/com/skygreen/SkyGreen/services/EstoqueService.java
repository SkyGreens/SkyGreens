package com.skygreen.SkyGreen.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.skygreen.SkyGreen.entities.EstoqueEntity;
import com.skygreen.SkyGreen.repositories.EstoqueRepository;

import jakarta.persistence.EntityNotFoundException;

@Service
public class EstoqueService {
    
   @Autowired
   private EstoqueRepository repository;
   
   public List<EstoqueEntity> listar(){
    return repository.findAll();
   }

   public EstoqueEntity findById(Integer id){
    return repository.findById(id).orElseThrow(() -> new EntityNotFoundException("User not found with id " + id));
   }
}
