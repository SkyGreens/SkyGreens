package com.skygreen.SkyGreen.services.interfaces;

import java.util.List;

import com.skygreen.SkyGreen.entities.PedidoVendaEntity;

public interface IPedidoVendaService {

    PedidoVendaEntity criarVenda(PedidoVendaEntity pedidoVenda) throws Exception;

    List<PedidoVendaEntity> getVenda();

}