package com.skygreen.SkyGreen.services.interfaces;

import java.util.List;

import com.skygreen.SkyGreen.entities.PedidoCompraEntity;

public interface IPedidoCompraService {

    PedidoCompraEntity criarPedido(PedidoCompraEntity pedidoCompra);

    List<PedidoCompraEntity> getPedidos();

}