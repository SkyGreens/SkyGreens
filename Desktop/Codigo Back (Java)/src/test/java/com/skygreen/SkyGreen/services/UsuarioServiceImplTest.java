package com.skygreen.SkyGreen.services;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.mockito.Mockito.when;
import static org.mockito.Mockito.verify;

import com.skygreen.SkyGreen.entities.UsuarioEntity;
import com.skygreen.SkyGreen.entities.UsuarioRole;
import com.skygreen.SkyGreen.repositories.UsuarioRepository;

import jakarta.persistence.EntityNotFoundException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Optional;

@ExtendWith(MockitoExtension.class)
public class UsuarioServiceImplTest {

    @Mock
    private UsuarioRepository repository;

    @InjectMocks
    private UsuarioServiceImpl usuarioService;

    private UsuarioEntity usuarioAtivo;

    @BeforeEach
    void setUp() {
        usuarioAtivo = new UsuarioEntity();
        usuarioAtivo.setId(1);
        usuarioAtivo.setNome("Teste");
        usuarioAtivo.setAtivo(true);
        usuarioAtivo.setEmail("teste@gmail.com");
        usuarioAtivo.setSenha("123456");
        usuarioAtivo.setRole(UsuarioRole.ADMIN);
    }

    @Test
    void testInativarUsuario_Success() {
        // Simula o repositório retornando o usuário ativo ao buscar por ID
        when(repository.findById(1)).thenReturn(Optional.of(usuarioAtivo));

        // Chama o método que inativa o usuário
        usuarioService.inativarUsuario(1);

        // Verifica se o campo 'ativo' foi alterado para 'false'
        assertFalse(usuarioAtivo.getAtivo(), "O usuário deve estar inativo");

        // Verifica se o repositório foi chamado para salvar o usuário
        verify(repository).save(usuarioAtivo);
    }

    @Test
    void testInativarUsuario_NotFound() {
        // Simula o repositório retornando vazio ao buscar por um ID inexistente
        when(repository.findById(999)).thenReturn(Optional.empty());

        // Testa se o método lança uma exceção EntityNotFoundException
        org.junit.jupiter.api.Assertions.assertThrows(EntityNotFoundException.class, () -> {
            usuarioService.inativarUsuario(999);
        });
    }
}
