package com.skygreen.SkyGreen.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Table(name = "prateleira")
@Entity(name = "prateleira")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class PrateleiraEntity {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer prateleira_id;

    @Column(unique = true, nullable = false)
    private String nome;

    private boolean disponivel;

    public PrateleiraEntity(String nome, boolean disponivel) {
        this.nome = nome;
        this.disponivel = disponivel;
    }
}
