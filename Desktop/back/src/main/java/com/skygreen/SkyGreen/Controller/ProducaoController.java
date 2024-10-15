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

import com.skygreen.SkyGreen.entities.ProducaoEntity;
import com.skygreen.SkyGreen.services.interfaces.IProducaoService;

import jakarta.transaction.Transactional;

@RestController
@RequestMapping("/producao")
public class ProducaoController {

    @Autowired
    private IProducaoService producaoService;

    @GetMapping("/")
    public ResponseEntity<List<ProducaoEntity>> findAll(){

        return ResponseEntity.ok().body(producaoService.findAll());
    }

    @GetMapping(value = "/{id}")
    public ResponseEntity<Optional<ProducaoEntity>> findById(@PathVariable Integer id) {
        Optional<ProducaoEntity> result = producaoService.findById(id);
        return ResponseEntity.ok().body(result);
    }

    @Transactional
    @PostMapping("/adicionar")
    public ResponseEntity<ProducaoEntity> add(@RequestBody ProducaoEntity producaoEntity) throws Exception{

        producaoEntity = producaoService.add(producaoEntity);
        return ResponseEntity.ok().body(producaoEntity);
    }

    @Transactional
    @DeleteMapping(value = "/delete/{id}")
    public ResponseEntity<Void> deleteProducao(@PathVariable int id) {

        producaoService.delete(id);
        return ResponseEntity.ok().build();
    }

    @Transactional
    @PutMapping("/update")
    public ResponseEntity<ProducaoEntity> updateProducao(@RequestBody ProducaoEntity producao) throws Exception{

        ProducaoEntity producaoAtualizado = producaoService.update(producao);
        return ResponseEntity.ok().body(producaoAtualizado);
    }

}
