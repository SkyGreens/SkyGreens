package com.skygreen.SkyGreen.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Repository;


import com.skygreen.SkyGreen.entities.FuncionarioEntity;

@Repository
public interface FuncionarioRepository extends JpaRepository<FuncionarioEntity, Integer> {
    
   UserDetails findByCpf(String cpf);
}
