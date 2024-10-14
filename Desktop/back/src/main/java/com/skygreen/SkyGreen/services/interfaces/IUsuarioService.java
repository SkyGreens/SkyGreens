package com.skygreen.SkyGreen.services.interfaces;

import java.nio.file.AccessDeniedException;
import java.util.List;

import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;

import com.skygreen.SkyGreen.entities.UsuarioEntity;

public interface IUsuarioService {

    List<UsuarioEntity> findAll();

    UsuarioEntity add(UsuarioEntity usuario);

    UsuarioEntity findById(Integer id);

    void delete(Integer id);

    UsuarioEntity updateUsuario(UsuarioEntity usuario);

    UserDetails loadUserByUsername(String cpf) throws UsernameNotFoundException;

    UsuarioEntity inativarUsuario(Integer id);

    UsuarioEntity ativarUsuario(Integer id);

    UsuarioEntity selfProfile (Integer idUsuarioLogado, Integer idRequisitado) throws AccessDeniedException;

    UsuarioEntity findByCpf(String cpf);
}