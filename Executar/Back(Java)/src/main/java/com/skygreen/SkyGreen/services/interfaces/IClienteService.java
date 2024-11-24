package com.skygreen.SkyGreen.services.interfaces;

import java.util.List;
import java.util.Optional;

import com.skygreen.SkyGreen.entities.ClienteEntity;

public interface IClienteService {

    List<ClienteEntity> findAll();
 
    Optional<ClienteEntity> findById(Integer id);

    ClienteEntity add(ClienteEntity cliente);

    ClienteEntity update(ClienteEntity cliente);    
        
    void delete(Integer id);

}