package com.skygreen.SkyGreen.services;

import java.util.List;
import java.util.Optional;
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

    @Autowired
    private SementeServiceImpl sementeService;

    @Override
    public PedidoCompraEntity criarPedido(PedidoCompraEntity pedidoCompra) {
        // Verifica se a semente existe e obtém o fornecedor
        Optional<SementeEntity> sementeOptional = sementeService.findById(pedidoCompra.getSemente().getSementeId());

        // Se a semente não existir, lance uma exceção ou retorne um erro
        if (sementeOptional.isEmpty()) {
            throw new RuntimeException("Semente não encontrada.");
        }

        SementeEntity semente = sementeOptional.get();

        // Valida se o fornecedorId da semente é o mesmo do pedido
        if (!semente.getFornecedor().getFornecedorId().equals(pedidoCompra.getFornecedor().getFornecedorId())) {
            throw new RuntimeException("Fornecedor do pedido não corresponde ao fornecedor da semente.");
        }

        // Define a data do pedido
        pedidoCompra.setDataPedido(LocalDateTime.now());
        PedidoCompraEntity novoPedido = pedidoRepository.save(pedidoCompra);

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
