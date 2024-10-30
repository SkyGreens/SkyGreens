package com.skygreen.SkyGreen.services;

import java.util.List;
import java.util.ArrayList;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;

import com.skygreen.SkyGreen.entities.ClienteEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.repositories.ClienteRepository;
import com.skygreen.SkyGreen.repositories.SementeRepository;
import com.skygreen.SkyGreen.services.interfaces.IClienteService;

@Service
public class ClienteServiceImpl implements IClienteService {

    @Autowired
    private ClienteRepository repository;

    @Autowired
    private SementeRepository sementeRepository;

    @Override
    public List<ClienteEntity> findAll() {
        return repository.findAll();
    }

    @Override
    public ClienteEntity add(ClienteEntity cliente) {
        cliente = repository.save(cliente);
        return cliente;
    }

    @Override
    public Optional<ClienteEntity> findById(Integer id) {
        return repository.findById(id);
    }

    @Override
    public void delete(Integer id) {
        repository.deleteById(id);
    }

    @Override
    public ClienteEntity update(@RequestBody ClienteEntity cliente) {
        Optional<ClienteEntity> clienteExistente = repository.findById(cliente.getClienteId());

        clienteExistente.get().setAtivo(cliente.getAtivo()); 
        clienteExistente.get().setEmail(cliente.getEmail());
        clienteExistente.get().setTelefone(cliente.getTelefone());
        clienteExistente.get().setEndereco(cliente.getEndereco());
        clienteExistente.get().setCidade(cliente.getCidade());
        clienteExistente.get().setEstado(cliente.getEstado()); 
        clienteExistente.get().setPais(cliente.getPais());
        clienteExistente.get().setRazaoSocial(cliente.getRazaoSocial());
        clienteExistente.get().setCnpj(cliente.getCnpj());

        cliente = repository.save(clienteExistente.get());
        return cliente;
    }
}
