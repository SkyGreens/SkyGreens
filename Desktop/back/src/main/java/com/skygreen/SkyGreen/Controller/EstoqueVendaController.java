package com.skygreen.SkyGreen.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.skygreen.SkyGreen.entities.ProducaoEntity;
import com.skygreen.SkyGreen.services.interfaces.IProducaoService;

@RestController
@RequestMapping("/estoquevenda")
public class EstoqueVendaController {
    
    @Autowired
    private IProducaoService producaoService;

    @GetMapping("/")
    public ResponseEntity<List<ProducaoEntity>> listarEstoqueVenda(){
        return ResponseEntity.ok().body(producaoService.listarEstoqueVenda());
    } 
}
