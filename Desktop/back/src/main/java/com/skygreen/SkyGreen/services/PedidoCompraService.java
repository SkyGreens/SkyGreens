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

@Service
public class PedidoCompraService {

    @Autowired
    private PedidoCompraRepository pedidoRepository;

    @Autowired
    private SementeRepository sementeRepository;

    @Autowired
    private EstoqueRepository estoqueRepository;

    public PedidoCompraEntity criarPedido(PedidoCompraEntity pedidoCompra) {
        // Salvando o pedido de compra
        PedidoCompraEntity novoPedido = pedidoRepository.save(pedidoCompra);

        // Atualizando o estoque da semente
        SementeEntity semente = novoPedido.getSemente();
        EstoqueEntity estoque = semente.getEstoque();

        if (estoque == null) {
            // Se o estoque não existir, cria um novo
            estoque = new EstoqueEntity();
            estoque.setSemente(semente);
            estoque.setQuantidade(novoPedido.getQuantidade());
        } else {
            // Se o estoque já existir, incrementa a quantidade
            estoque.setQuantidade(estoque.getQuantidade() + novoPedido.getQuantidade());
        }

        estoqueRepository.save(estoque);

        return novoPedido;
    }
    
    public List<PedidoCompraEntity> getPedidos() {
        return pedidoRepository.findAll();
    }
}

