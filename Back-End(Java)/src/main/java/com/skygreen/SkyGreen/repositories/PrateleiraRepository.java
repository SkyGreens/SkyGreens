package com.skygreen.SkyGreen.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;
import com.skygreen.SkyGreen.entities.PrateleiraEntity;

@Repository
public interface PrateleiraRepository extends JpaRepository<PrateleiraEntity, Integer> {

    Optional<PrateleiraEntity> findByNome(String nome);
    
    List<PrateleiraEntity> findByDisponivelTrue();
    
}
