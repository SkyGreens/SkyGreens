package com.skygreen.SkyGreen.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.skygreen.SkyGreen.entities.EstoqueEntity;
import com.skygreen.SkyGreen.entities.PedidoCompraEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.repositories.EstoqueRepository;
import com.skygreen.SkyGreen.repositories.PedidoCompraRepository;
import com.skygreen.SkyGreen.repositories.SementeRepository;
import com.skygreen.SkyGreen.services.interfaces.IPedidoCompraService;

@Service
public class PedidoCompraServiceImpl implements IPedidoCompraService {

    @Autowired
    private PedidoCompraRepository pedidoRepository;

    @Autowired
    private SementeRepository sementeRepository;

    @Autowired
    private EstoqueRepository estoqueRepository;

    @Override
    public PedidoCompraEntity criarPedido(PedidoCompraEntity pedidoCompra) {

        PedidoCompraEntity novoPedido = pedidoRepository.save(pedidoCompra);

        SementeEntity semente = novoPedido.getSemente();
        EstoqueEntity estoque = semente.getEstoque();

        if (estoque == null) {
            estoque = new EstoqueEntity();
            estoque.setSemente(semente);
            estoque.setQuantidade(novoPedido.getQuantidade());
        } else {
            estoque.setQuantidade(estoque.getQuantidade() + novoPedido.getQuantidade());
        }

        estoqueRepository.save(estoque);

        return novoPedido;
    }

    @Override
    public List<PedidoCompraEntity> getPedidos() {
        return pedidoRepository.findAll();
    }
}
