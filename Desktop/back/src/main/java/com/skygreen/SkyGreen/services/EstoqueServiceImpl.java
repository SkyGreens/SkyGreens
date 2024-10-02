package com.skygreen.SkyGreen.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.skygreen.SkyGreen.entities.EstoqueEntity;
import com.skygreen.SkyGreen.repositories.EstoqueRepository;
import com.skygreen.SkyGreen.services.interfaces.IEstoqueService;

import jakarta.persistence.EntityNotFoundException;

@Service
public class EstoqueServiceImpl implements IEstoqueService {

   @Autowired
   private EstoqueRepository repository;

   @Override
   public List<EstoqueEntity> listar() {
      return repository.findAll();
   }

   @Override
   public EstoqueEntity findById(Integer id) {
      return repository.findById(id).orElseThrow(() -> new EntityNotFoundException("User not found with id " + id));
   }
}
