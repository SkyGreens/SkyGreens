package com.skygreen.SkyGreen.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.services.interfaces.ISementeService;

@RestController
@RequestMapping("/sementes")
public class SementeController {

    @Autowired
    private ISementeService sementeService;

    @GetMapping("/listar")
    public List<SementeEntity> getAllSementes() {
        return sementeService.findAll();
    }

    @PostMapping("/adicionar")
    public SementeEntity criarSemente(@RequestBody SementeEntity semente) {
        return sementeService.criarSemente(semente);
    }
}
