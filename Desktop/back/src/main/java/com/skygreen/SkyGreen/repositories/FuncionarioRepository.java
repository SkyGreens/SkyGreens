package com.skygreen.SkyGreen.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

import com.skygreen.SkyGreen.entities.FuncionarioEntity;

@Repository
public interface FuncionarioRepository extends JpaRepository<FuncionarioEntity, Integer> {
    
    public Optional<FuncionarioEntity> findByEmailAndSenha(String email, String senha);
}
