package com.skygreen.SkyGreen.services;

import java.util.List;
import java.util.Optional;
import java.time.LocalDateTime;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.skygreen.SkyGreen.entities.ClienteEntity;
import com.skygreen.SkyGreen.entities.EstoqueEntity;
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

import java.util.Date;

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
    private EstoqueRepository estoqueRepository;

    @Autowired
    private ProducaoRepository producaoRepository;

    @Override
    public PedidoVendaEntity criarVenda(PedidoVendaEntity pedidoVenda) throws Exception{
        
        ProducaoEntity novaProducao = criaProducaoEntity(pedidoVenda);
        
        Optional<SementeEntity> semente = sementeRepository.findById(pedidoVenda.getSemente().getSementeId());
        //valida se semente existe
        if(!semente.isPresent()){
            throw new Exception("Id de semente não encontrado.");
        }
        
        //valida se tem semente disponível para venda
        if(pedidoVenda.getQuantidade() >= semente.get().getEstoque().getQuantidade()){
            throw new Exception("Id de semente não encontrado.");
        }

        EstoqueEntity novoEstoque = new EstoqueEntity();
        novoEstoque.setEstoqueId(semente.get().getEstoque().getEstoqueId());
        novoEstoque.setSemente(semente.get());
        novoEstoque.setQuantidade(semente.get().getEstoque().getQuantidade() - pedidoVenda.getQuantidade());

        List<PrateleiraEntity> prateleirasDisponiveis = prateleiraRepository.findByDisponivelTrue();
        //valida se tem prateleira disponível
        if(prateleirasDisponiveis.size() < 1){
            throw new Exception("Nenhuma prateleira disponível!");
        }
        
        PrateleiraEntity prateleiraUtilizada = prateleirasDisponiveis.get(0);
        prateleiraUtilizada.setDisponivel(false);
        
        novaProducao.setPrateleira(prateleiraUtilizada);
        
        Optional<ClienteEntity> cliente = clienteRepository.findById(pedidoVenda.getCliente().getClienteId());
        
        //valida se cliente existe
        if (!cliente.isPresent()){
            throw new Exception ("Id de cliente não encontrado.");
        }
        
        estoqueRepository.save(novoEstoque);       
        prateleiraRepository.save(prateleiraUtilizada);
        producaoRepository.save(novaProducao);

        return pedidoVendaRepository.save(pedidoVenda);
    }

    private ProducaoEntity criaProducaoEntity(PedidoVendaEntity pedidoVenda){
        //criar nova producao
        ProducaoEntity novaProducao = new ProducaoEntity();

        novaProducao.setSementeId(pedidoVenda.getSemente().getSementeId());
        novaProducao.setSementeQuantidade(pedidoVenda.getQuantidade());
        novaProducao.setTempoCultivo(pedidoVenda.getTempoCultivo());
        novaProducao.setDataInicio(new Date());
        novaProducao.setAtivo(true);

        return novaProducao;
    }

    @Override
    public List<PedidoVendaEntity> getVenda() {
        return pedidoVendaRepository.findAll();
    }
}
