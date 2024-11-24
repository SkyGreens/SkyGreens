package com.skygreen.SkyGreen.entities;

import java.io.Serializable;
import java.util.Calendar;
import java.util.Date;

import com.fasterxml.jackson.annotation.JsonBackReference;

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
    private int producaoId;

    private Integer sementeId; 
    private Integer sementeQuantidade; 

    private Integer tempoCultivo;
    private Date dataInicio;

    private String fotoSemente;

    private Boolean ativo;

    @OneToOne
    @JoinColumn(name = "prateleira_id")
    @JsonBackReference
    private PrateleiraEntity prateleira;

    public Date getDataFim(){
        Date dt = this.dataInicio;
        Calendar c = Calendar.getInstance(); 
        c.setTime(dt); 
        c.add(Calendar.DATE, this.tempoCultivo);
        dt = c.getTime();
        return dt;
    }

    public Boolean getAtivo(){
        if(getDataFim().before(new Date())){
            return false;
        } else{
            return this.ativo;
        }
    }
}
