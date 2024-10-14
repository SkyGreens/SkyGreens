package com.skygreen.SkyGreen.entities;

import java.io.Serializable;
import java.util.Date;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity(name = "producao")
@Table(name = "producao")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class ProducaoEntity implements Serializable{
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int Integer;

    private Integer sementeId; 
    private Integer sementeQuantidade; 

    private Integer tempoCultivo;
    private Date dataInicio;

    private String fotoSemente;

    private Boolean ativo;

    @OneToOne
    @JoinColumn(name = "prateleira_id")
    private PrateleiraEntity prateleira;
}
