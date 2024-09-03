package com.skygreen.SkyGreen.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;
import java.util.Optional;
import com.skygreen.SkyGreen.entities.FuncionarioEntity;
import com.skygreen.SkyGreen.repositories.FuncionarioRepository;
import com.skygreen.SkyGreen.services.interfaces.IFuncionarioService;

import jakarta.persistence.EntityNotFoundException;

@Service
public class FuncionarioServiceImpl implements IFuncionarioService {

    @Autowired
    private FuncionarioRepository repository;
    
    @Override
    public List<FuncionarioEntity> findAll(){
        return repository.findAll();
    }

    @Override
    public FuncionarioEntity add(FuncionarioEntity funcionario){
        funcionario = repository.save(funcionario);
        return funcionario;
    }

    @Override
    public FuncionarioEntity findById(Integer id){
       return repository.findById(id)
       .orElseThrow(() -> new EntityNotFoundException("User not found with id " + id));
    }

    @Override
    public void delete(Integer id){
        repository.deleteById(id);
    }

    @Override
    public FuncionarioEntity updateFuncionario(@RequestBody FuncionarioEntity funcionario){

        funcionario = repository.findById(funcionario.getId()).orElse(null);

        funcionario.setAtivo(funcionario.getAtivo());
        funcionario.setCargo_id(funcionario.getCargo_id());
        funcionario.setCpf(funcionario.getCpf());
        funcionario.setEmail(funcionario.getEmail());
        funcionario.setId(funcionario.getId());
        funcionario.setNome(funcionario.getNome());
        funcionario.setSenha(funcionario.getSenha());
        
        funcionario = repository.save(funcionario);
        return funcionario;
    }

    public FuncionarioEntity FindByEmailAndSenha(String email, String senha){

        Optional<FuncionarioEntity> funcionario = repository.findByEmailAndSenha(email, senha);
        if(funcionario.isPresent()){
            return funcionario.get();
        }
        else{
            return null;
        }
    }


}
