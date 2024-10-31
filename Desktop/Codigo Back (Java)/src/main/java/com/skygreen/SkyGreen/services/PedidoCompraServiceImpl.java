package com.skygreen.SkyGreen.services;

import java.util.List;
import java.time.LocalDateTime;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.skygreen.SkyGreen.entities.EstoqueEntity;
import com.skygreen.SkyGreen.entities.PedidoCompraEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.repositories.EstoqueRepository;
import com.skygreen.SkyGreen.repositories.PedidoCompraRepository;
import com.skygreen.SkyGreen.services.interfaces.IPedidoCompraService;

@Service
public class PedidoCompraServiceImpl implements IPedidoCompraService {

    @Autowired
    private PedidoCompraRepository pedidoRepository;

    @Autowired
    private EstoqueRepository estoqueRepository;

    @Override
    public PedidoCompraEntity criarPedido(PedidoCompraEntity pedidoCompra) {

        pedidoCompra.setDataPedido(LocalDateTime.now());
        PedidoCompraEntity novoPedido = pedidoRepository.save(pedidoCompra);

        SementeEntity semente = novoPedido.getSemente();
        List<EstoqueEntity> estoque = estoqueRepository.findBySemente(semente);

        if (estoque.isEmpty()) {
            EstoqueEntity novoEstoque = new EstoqueEntity();
            novoEstoque.setSemente(semente);
            novoEstoque.setQuantidade(novoPedido.getQuantidade());
            estoqueRepository.save(novoEstoque);
        } else {
            EstoqueEntity estoqueExistente = estoque.get(0); // Pega o primeiro estoque encontrado
            estoqueExistente.setQuantidade(estoqueExistente.getQuantidade() + novoPedido.getQuantidade());
            estoqueRepository.save(estoqueExistente);
        }

        return novoPedido;
    }

    @Override
    public List<PedidoCompraEntity> getPedidos() {
        return pedidoRepository.findAll();
    }
}
