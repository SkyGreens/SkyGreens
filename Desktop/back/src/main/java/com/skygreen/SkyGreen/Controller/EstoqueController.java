package com.skygreen.SkyGreen.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.skygreen.SkyGreen.entities.EstoqueEntity;
import com.skygreen.SkyGreen.services.interfaces.IEstoqueService;

@RestController
@RequestMapping("/estoque")
public class EstoqueController {
    
    @Autowired
    private IEstoqueService service;


    @GetMapping("/")
    public ResponseEntity<List<EstoqueEntity>> listar(){
        return ResponseEntity.ok().body(service.listar());
    } 

    @GetMapping("/{id}")
    public ResponseEntity<EstoqueEntity> findById(@RequestParam Integer id){
        return ResponseEntity.ok().body(service.findById(id));
    }
}
