package com.skygreen.SkyGreen.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;

import com.skygreen.SkyGreen.entities.FuncionarioEntity;
import com.skygreen.SkyGreen.repositories.FuncionarioRepository;

import jakarta.persistence.EntityNotFoundException;

@Service
public class FuncionarioServiceImpl implements UserDetailsService {

    @Autowired
    private FuncionarioRepository repository;

    public List<FuncionarioEntity> findAll() {
        return repository.findAll();
    }

    public FuncionarioEntity add(FuncionarioEntity funcionario) {
        funcionario = repository.save(funcionario);
        return funcionario;
    }

    public FuncionarioEntity findById(Integer id) {
        return repository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("User not found with id " + id));
    }

    public void delete(Integer id) {
        repository.deleteById(id);
    }

    public FuncionarioEntity updateFuncionario(@RequestBody FuncionarioEntity funcionario) {

        funcionario = repository.findById(funcionario.getId()).orElse(null);

        funcionario.setAtivo(funcionario.getAtivo());
        funcionario.setRole(funcionario.getRole());
        funcionario.setCpf(funcionario.getCpf());
        funcionario.setEmail(funcionario.getEmail());
        funcionario.setId(funcionario.getId());
        funcionario.setNome(funcionario.getNome());
        funcionario.setSenha(funcionario.getSenha());

        funcionario = repository.save(funcionario);
        return funcionario;
    }

    @Override
    public UserDetails loadUserByUsername(String cpf) throws UsernameNotFoundException {
        return repository.findByCpf(cpf);
    }

}
