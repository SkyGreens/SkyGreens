package com.skygreen.SkyGreen.Controller;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.skygreen.SkyGreen.entities.ClienteEntity;
import com.skygreen.SkyGreen.services.interfaces.IClienteService;

import jakarta.transaction.Transactional;

@RestController
@RequestMapping("/cliente")
public class ClienteController {

    @Autowired
    private IClienteService clienteService;

    @GetMapping("/")
    public ResponseEntity<List<ClienteEntity>> findAll(){

        return ResponseEntity.ok().body(clienteService.findAll());
    }

    @GetMapping(value = "/{id}")
    public ResponseEntity<Optional<ClienteEntity>> findById(@PathVariable Integer id) {
        Optional<ClienteEntity> result = clienteService.findById(id);
        return ResponseEntity.ok().body(result);
    }

    @Transactional
    @PostMapping("/adicionar")
    public ResponseEntity<ClienteEntity> add(@RequestBody ClienteEntity clienteEntity) {

        clienteEntity = clienteService.add(clienteEntity);
        return ResponseEntity.ok().body(clienteEntity);
    }

    @Transactional
    @DeleteMapping(value = "/delete/{id}")
    public ResponseEntity<Void> deleteCliente(@PathVariable int id) {

        clienteService.delete(id);
        return ResponseEntity.ok().build();
    }

    @Transactional
    @PutMapping("/update")
    public ResponseEntity<ClienteEntity> updateCliente(@RequestBody ClienteEntity cliente) {

        ClienteEntity clienteAtualizado = clienteService.update(cliente);
        return ResponseEntity.ok().body(clienteAtualizado);
    }
}
