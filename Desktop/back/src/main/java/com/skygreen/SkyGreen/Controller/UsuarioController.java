package com.skygreen.SkyGreen.Controller;

import java.nio.file.AccessDeniedException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.skygreen.SkyGreen.entities.UsuarioEntity;
import com.skygreen.SkyGreen.services.interfaces.IUsuarioService;

import jakarta.transaction.Transactional;

@RestController
@RequestMapping("/usuario")
public class UsuarioController {

    @Autowired
    private IUsuarioService usuarioService;

    @GetMapping("/listar")
    public ResponseEntity<List<UsuarioEntity>> findAll() {

        return ResponseEntity.ok().body(usuarioService.findAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<UsuarioEntity> findById(@PathVariable Integer id) {
        UsuarioEntity result = usuarioService.findById(id);
        return ResponseEntity.ok().body(result);
    }

    @Transactional
    @DeleteMapping("/delete/{id}")
    public ResponseEntity<Void> deleteUsuario(@PathVariable int id) {

        usuarioService.delete(id);
        return ResponseEntity.ok().build();
    }

    @Transactional
    @PutMapping("/update")
    public ResponseEntity<UsuarioEntity> updateUsuario(@RequestBody UsuarioEntity usuario) {

        UsuarioEntity usuarioAtualizado = usuarioService.updateUsuario(usuario);
        return ResponseEntity.ok().body(usuarioAtualizado);
    }

    @PutMapping("/inativar/{id}")
    public ResponseEntity<UsuarioEntity> inativarUsuario(@PathVariable Integer id) {
        UsuarioEntity usuarioInativado = usuarioService.inativarUsuario(id);
        return ResponseEntity.ok(usuarioInativado);
    }

    @PutMapping("/ativar/{id}")
    public ResponseEntity<UsuarioEntity> ativarUsuario(@PathVariable Integer id) {
        UsuarioEntity usuarioAtivo = usuarioService.ativarUsuario(id);
        return ResponseEntity.ok(usuarioAtivo);
    }

    @GetMapping("/personal/{id}")
    public ResponseEntity<UsuarioEntity> selfProfile(@PathVariable Integer id,
            @AuthenticationPrincipal UserDetails userDetails) throws AccessDeniedException {
        String cpf = userDetails.getUsername();

        UsuarioEntity usuarioLogado = usuarioService.findByCpf(cpf);
        Integer idUsuarioLogado = usuarioLogado.getId();

        UsuarioEntity result = usuarioService.selfProfile(idUsuarioLogado, id);
        return ResponseEntity.ok().body(result);
    }

}