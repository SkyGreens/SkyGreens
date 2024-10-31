package com.skygreen.SkyGreen.DTO;

import com.skygreen.SkyGreen.entities.UsuarioRole;

public record RegisterDTO(String cpf, String senha, UsuarioRole role, String email, boolean ativo, String nome  ) {
      
}
