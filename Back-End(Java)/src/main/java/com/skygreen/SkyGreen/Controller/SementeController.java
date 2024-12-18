package com.skygreen.SkyGreen.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.services.interfaces.ISementeService;

import jakarta.transaction.Transactional;

@RestController
@RequestMapping("/sementes")
public class SementeController {

    @Autowired
    private ISementeService sementeService;

    @GetMapping("/")
    public List<SementeEntity> getAllSementes() {
        return sementeService.findAll();
    }

    @PostMapping("/adicionar")
    public SementeEntity criarSemente(@RequestBody SementeEntity semente) {
        return sementeService.criarSemente(semente);
    }

    @Transactional
    @DeleteMapping("/delete/{id}")
    public ResponseEntity<Void> delete(@PathVariable Integer id) {

        sementeService.delete(id);
        return ResponseEntity.ok().build();
    }
}
