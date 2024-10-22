package com.skygreen.SkyGreen.services;

import java.util.List;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Date;
import java.util.Optional;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;

import com.skygreen.SkyGreen.entities.EstoqueEntity;
import com.skygreen.SkyGreen.entities.PrateleiraEntity;
import com.skygreen.SkyGreen.entities.ProducaoEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.repositories.SementeRepository;
import com.skygreen.SkyGreen.repositories.PrateleiraRepository;
import com.skygreen.SkyGreen.repositories.ProducaoRepository;
import com.skygreen.SkyGreen.services.interfaces.IProducaoService;

@Service
public class ProducaoServiceImpl implements IProducaoService {

    @Autowired
    private ProducaoRepository producaoRepository;

    @Autowired
    private SementeRepository sementeRepository;

    @Autowired
    private PrateleiraRepository prateleiraRepository;

    @Override
    public List<ProducaoEntity> findAll() {
        return producaoRepository.findAll();
    }

    
    @Override
    public ProducaoEntity add(ProducaoEntity producao) throws Exception{
        Optional<SementeEntity> semente = sementeRepository.findById(producao.getSementeId());
        
        //validar se a semente a válida
        if(!semente.isPresent()){
            throw new Exception("Id de semente não encontrado.");
        }
        
        //validar se a semente possui quantidade suficiente 
        if(semente.get().getEstoque().getQuantidade() < producao.getSementeQuantidade()){
            throw new Exception("Sem estoque disponível para a quantidade de semente escolhida.");
        }

        List<PrateleiraEntity> prateleirasDisponiveis = prateleiraRepository.findByDisponivelTrue();

        if(prateleirasDisponiveis.size() < 1){
            throw new Exception("Nenhuma prateleira disponível!");
        }

        //Ocupar uma prateleira
        PrateleiraEntity prateleiraEscolhida = prateleirasDisponiveis.get(0);


        if(producao.getDataFim().after(new Date())){
            prateleiraEscolhida.setProducao(producao);
            prateleiraEscolhida.setDisponivel(false);
            producao.setPrateleira(prateleiraEscolhida);
            //setar como ativo ao criar producao
            producao.setAtivo(true);
        }

        //pegando o estoque atual
        EstoqueEntity estoqueSemente = semente.get().getEstoque();
        //descontando quantidade de semente utilizada
        estoqueSemente.setQuantidade(estoqueSemente.getQuantidade() - producao.getSementeQuantidade());
        //pegando a semente
        SementeEntity sementeAtualizada = semente.get();
        //salvando o estoque da semente
        sementeAtualizada.setEstoque(estoqueSemente);
        //persistindo no banco a semente com estoque atualizado
        sementeAtualizada = sementeRepository.save(sementeAtualizada);
        
        producao = producaoRepository.save(producao);
        return producao;
    }

    @Override
    public Optional<ProducaoEntity> findById(Integer id) {
        return producaoRepository.findById(id);
    }

    @Override
    public void delete(Integer id) {
        producaoRepository.deleteById(id);
    }

    @Override
    public ProducaoEntity update(@RequestBody ProducaoEntity producao) throws Exception {

        Optional<ProducaoEntity> producaoExistente = producaoRepository.findById(producao.getProducaoId());
        
        //validar se a producao existe
        if(!producaoExistente.isPresent()){
            throw new Exception("Id de produção não encontrado!");
        }

        Optional<SementeEntity> semente = sementeRepository.findById(producao.getSementeId());
        
        //validar se a semente a válida
        if(!semente.isPresent()){
            throw new Exception("Id de semente não encontrado.");
        }
        
        //validar se a semente possui quantidade suficiente 
        if(semente.get().getEstoque().getQuantidade() < producao.getSementeQuantidade()){
            throw new Exception("Sem estoque disponível para a quantidade de semente escolhida.");
        }

        producaoExistente.get().setAtivo(producao.getAtivo());
        producaoExistente.get().setTempoCultivo(producao.getTempoCultivo());

        producao = producaoRepository.save(producaoExistente.get());
        return producao;
    }

    @Override
    public List<ProducaoEntity> listarEstoqueVenda() {
        List<ProducaoEntity> producao = producaoRepository.findAll();

        List<ProducaoEntity> producoesFinalizadas = producao.stream().filter(p -> !p.getAtivo()).collect(Collectors.toList());
        
        return producoesFinalizadas;
    }

}
