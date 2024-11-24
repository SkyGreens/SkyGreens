package com.skygreen.SkyGreen.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.skygreen.SkyGreen.entities.PrateleiraEntity;
import com.skygreen.SkyGreen.services.interfaces.IPrateleiraService;

@RestController
@RequestMapping("/prateleira")
public class PrateleiraController {

    @Autowired
    private IPrateleiraService service;

    @GetMapping("/disponiveis")
    public ResponseEntity<List<PrateleiraEntity>> listarPrateleirasDisponiveis() {
        return ResponseEntity.ok().body(service.listarPrateleirasDisponiveis());
    }

    @PostMapping("/alocar/{id}")
    public ResponseEntity<PrateleiraEntity> alocarPrateleira(@PathVariable int id) throws Exception {
        PrateleiraEntity prateleira = service.alocarPrateleiraParaProducao(id);
        return ResponseEntity.status(HttpStatus.OK).body(prateleira);
    }

    @PostMapping("/liberar/{id}")
    public ResponseEntity<String> liberarPrateleira(@PathVariable int id) {
        try {
            service.liberarPrateleira(id);
            return ResponseEntity.status(HttpStatus.OK).body("Prateleira liberada com sucesso.");
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Prateleira não encontrada.");
        }
    }
    @GetMapping("/")
    public ResponseEntity<List<PrateleiraEntity>> listar(){

    return ResponseEntity.ok().body(service.listar());
    }
}
