package com.skygreen.SkyGreen.services.interfaces;

import java.util.List;

import com.skygreen.SkyGreen.entities.FuncionarioEntity;

public interface IFuncionarioService {

    List<FuncionarioEntity> findAll();

    FuncionarioEntity add(FuncionarioEntity funcionario);

    FuncionarioEntity findById(Integer id);

    void delete(Integer id);

    FuncionarioEntity updateFuncionario(FuncionarioEntity funcionario);

    public FuncionarioEntity FindByEmailAndSenha(String email, String senha);
}