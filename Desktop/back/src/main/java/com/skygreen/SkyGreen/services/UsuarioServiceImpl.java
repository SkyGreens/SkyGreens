package com.skygreen.SkyGreen.services;

import java.nio.file.AccessDeniedException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;

import com.skygreen.SkyGreen.entities.UsuarioEntity;
import com.skygreen.SkyGreen.repositories.UsuarioRepository;
import com.skygreen.SkyGreen.services.interfaces.IUsuarioService;

import jakarta.persistence.EntityNotFoundException;

@Service
public class UsuarioServiceImpl implements UserDetailsService, IUsuarioService {

    @Autowired
    private UsuarioRepository repository;

    @Override
    public List<UsuarioEntity> findAll() {
        return repository.findAll();
    }

    @Override
    public UsuarioEntity add(UsuarioEntity usuario) {
        usuario = repository.save(usuario);
        return usuario;
    }

    @Override
    public UsuarioEntity findById(Integer id) {
        return repository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("User not found with id " + id));
    }

    @Override
    public void delete(Integer id) {
        repository.deleteById(id);
    }

    @Override
    public UsuarioEntity inativarUsuario(@PathVariable Integer id) {
        UsuarioEntity usuarioExistente = repository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Usuário não encontrado com id " + id));

        usuarioExistente.setAtivo(false);

        return repository.save(usuarioExistente);
    }

    @Override
    public UsuarioEntity ativarUsuario(@PathVariable Integer id) {
        UsuarioEntity usuario = repository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Usuário não encontrado com o id" + id));

        usuario.setAtivo(true);
        return repository.save(usuario);
    }

    @Override
public UsuarioEntity updateUsuario(@RequestBody UsuarioEntity usuario) {

    UsuarioEntity usuarioAntigo = repository.findById(usuario.getId()).orElse(null);

    if (usuarioAntigo != null) {
        usuarioAntigo.setAtivo(usuario.getAtivo());
        usuarioAntigo.setRole(usuario.getRole());
        usuarioAntigo.setEmail(usuario.getEmail());
        usuarioAntigo.setId(usuario.getId());
        usuarioAntigo.setNome(usuario.getNome());
        
        // Não alteramos o CPF e a senha
        // usuarioAntigo.setCpf(usuario.getCpf());
        // usuarioAntigo.setSenha(usuario.getSenha());

        usuario = repository.save(usuarioAntigo);
    }

    return usuario;
}

    @Override
    public UserDetails loadUserByUsername(String cpf) throws UsernameNotFoundException {
        return repository.findUsuarioByCpf(cpf);

    }

    @Override
    public UsuarioEntity selfProfile(Integer idUsuarioLogado, Integer idRequisitado) throws AccessDeniedException {
        if (!idUsuarioLogado.equals(idRequisitado)) {
            throw new AccessDeniedException("Você não tem permissão para acessar este perfil.");
        }

        return repository.findById(idRequisitado)
                .orElseThrow(() -> new EntityNotFoundException("Usuário não encontrado com o id " + idRequisitado));
    }

    @Override
    public UsuarioEntity findByCpf(String cpf) {
        return repository.findByCpf(cpf)
                .orElseThrow(() -> new EntityNotFoundException("Usuário não encontrado com o CPF " + cpf));
    }

}
