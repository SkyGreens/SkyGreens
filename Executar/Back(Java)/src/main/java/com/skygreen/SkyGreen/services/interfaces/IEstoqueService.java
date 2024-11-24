package com.skygreen.SkyGreen.services.interfaces;

import java.util.List;

import com.skygreen.SkyGreen.entities.EstoqueEntity;

public interface IEstoqueService {

    List<EstoqueEntity> listar();

    EstoqueEntity findById(Integer id);

}