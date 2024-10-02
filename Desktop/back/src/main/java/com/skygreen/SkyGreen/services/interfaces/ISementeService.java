package com.skygreen.SkyGreen.services.interfaces;

import java.util.List;

import com.skygreen.SkyGreen.entities.SementeEntity;

public interface ISementeService {

    List<SementeEntity> findAll();

    SementeEntity getSementeById(Integer id);

    SementeEntity criarSemente(SementeEntity semente);

}