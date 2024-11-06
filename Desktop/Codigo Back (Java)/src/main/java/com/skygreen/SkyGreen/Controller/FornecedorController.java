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

import com.skygreen.SkyGreen.entities.FornecedorEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.services.interfaces.IFornecedorService;

import jakarta.transaction.Transactional;

@RestController
@RequestMapping("/fornecedor")
public class FornecedorController {

    @Autowired
    private IFornecedorService fornecedorService;

    @GetMapping("/")
    public ResponseEntity<List<FornecedorEntity>> findAll(){

        return ResponseEntity.ok().body(fornecedorService.findAll());
    }

    @GetMapping(value = "/{id}")
    public ResponseEntity<Optional<FornecedorEntity>> findById(@PathVariable Integer id) {
        Optional<FornecedorEntity> result = fornecedorService.findById(id);
        return ResponseEntity.ok().body(result);
    }

    @Transactional
    @PostMapping("/adicionar")
    public ResponseEntity<FornecedorEntity> add(@RequestBody FornecedorEntity fornecedorEntity) {

        fornecedorEntity = fornecedorService.add(fornecedorEntity);
        return ResponseEntity.ok().body(fornecedorEntity);
    }

    @Transactional
    @DeleteMapping(value = "/delete/{id}")
    public ResponseEntity<Void> deleteFornecedor(@PathVariable int id) {

        fornecedorService.delete(id);
        return ResponseEntity.ok().build();
    }

    @Transactional
    @PutMapping("/update")
    public ResponseEntity<FornecedorEntity> updateFornecedor(@RequestBody FornecedorEntity fornecedor) {

        FornecedorEntity fornecedorAtualizado = fornecedorService.update(fornecedor);
        return ResponseEntity.ok().body(fornecedorAtualizado);
    }

    @Transactional
    @PutMapping("/{fornecedorId}/sementes/adicionar")
    public ResponseEntity<FornecedorEntity> updateSemente(@PathVariable Integer fornecedorId, @RequestBody List<SementeEntity> sementes){

        return ResponseEntity.ok().body(fornecedorService.updateSementes(fornecedorId, sementes));
    }

    @Transactional
    @GetMapping("/{fornecedorId}/sementes")
    public ResponseEntity<List<SementeEntity>> getSementesPorFornecedor(@PathVariable int fornecedorId) {
        List<SementeEntity> sementes = fornecedorService.buscarSementePorFornecedor(fornecedorId);
        return ResponseEntity.ok(sementes);
    }

    @DeleteMapping("/{fornecedorId}/sementes/delete/{sementeId}")
public ResponseEntity<FornecedorEntity> removeSementeFromFornecedor(
        @PathVariable Integer fornecedorId,
        @PathVariable Integer sementeId) {
    FornecedorEntity fornecedorAtualizado = fornecedorService.removeSementeFromFornecedor(fornecedorId, sementeId);
    return ResponseEntity.ok(fornecedorAtualizado);
}

    }
