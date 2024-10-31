package com.skygreen.SkyGreen.services;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.Date;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.skygreen.SkyGreen.entities.ClienteEntity;
import com.skygreen.SkyGreen.entities.PedidoVendaEntity;
import com.skygreen.SkyGreen.entities.PrateleiraEntity;
import com.skygreen.SkyGreen.entities.ProducaoEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.repositories.ClienteRepository;
import com.skygreen.SkyGreen.repositories.EstoqueRepository;
import com.skygreen.SkyGreen.repositories.PedidoVendaRepository;
import com.skygreen.SkyGreen.repositories.PrateleiraRepository;
import com.skygreen.SkyGreen.repositories.ProducaoRepository;
import com.skygreen.SkyGreen.repositories.SementeRepository;
import com.skygreen.SkyGreen.services.interfaces.IPedidoVendaService;

@Service
public class PedidoVendaServiceImpl implements IPedidoVendaService {

    @Autowired
    private PedidoVendaRepository pedidoVendaRepository;

    @Autowired
    private ClienteRepository clienteRepository;

    @Autowired
    private SementeRepository sementeRepository;

    @Autowired
    private PrateleiraRepository prateleiraRepository;

    @Autowired
    private ProducaoRepository producaoRepository;

    @Autowired
    private ProducaoServiceImpl producaoServiceImpl;

    @Override
    public PedidoVendaEntity criarVenda(PedidoVendaEntity pedidoVenda) throws Exception {

        pedidoVenda.setDataPedido(LocalDateTime.now());
        Optional<SementeEntity> semente = sementeRepository.findById(pedidoVenda.getSemente().getSementeId());
        // valida se semente existe
        if (!semente.isPresent()) {
            throw new Exception("Id de semente não encontrado.");
        }
        
        // valida se tem semente disponível para venda
        if (pedidoVenda.getQuantidade() > semente.get().getEstoque().getQuantidade()) {
            throw new Exception("Quantidade de semente excedida.");
        }
        
        List<PrateleiraEntity> prateleirasDisponiveis = prateleiraRepository.findByDisponivelTrue();
        // valida se tem prateleira disponível
        if (prateleirasDisponiveis.size() < 1) {
            throw new Exception("Nenhuma prateleira disponível!");
        }
        ;
        
        Optional<ClienteEntity> cliente = clienteRepository.findById(pedidoVenda.getCliente().getClienteId());
        
        // valida se cliente existe
        if (!cliente.isPresent()) {
            throw new Exception("Id de cliente não encontrado.");
        }
        criaProducaoEntity(pedidoVenda);
        
        return pedidoVendaRepository.save(pedidoVenda);
    }

    private void criaProducaoEntity(PedidoVendaEntity pedidoVenda) throws Exception {
        ProducaoEntity novaProducao = new ProducaoEntity();

        novaProducao.setSementeId(pedidoVenda.getSemente().getSementeId());
        novaProducao.setSementeQuantidade(pedidoVenda.getQuantidade());
        novaProducao.setTempoCultivo(pedidoVenda.getTempoCultivo());

        LocalDateTime dataPedido = pedidoVenda.getDataPedido();
        if (dataPedido != null) {
            novaProducao.setDataInicio(Date.from(dataPedido.atZone(ZoneId.systemDefault()).toInstant()));
        } else {
            throw new IllegalArgumentException("Data do pedido não pode ser nula");
        }

        novaProducao.setAtivo(true);

        producaoServiceImpl.add(novaProducao);
        producaoRepository.save(novaProducao);
    }

    @Override
    public List<PedidoVendaEntity> getVenda() {
        return pedidoVendaRepository.findAll();
    }
}
