package com.skygreen.SkyGreen.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.skygreen.SkyGreen.entities.PrateleiraEntity;
import com.skygreen.SkyGreen.repositories.PrateleiraRepository;
import com.skygreen.SkyGreen.services.interfaces.IPrateleiraService;

@Service
public class PrateleiraServiceImpl implements IPrateleiraService {

    @Autowired
    private PrateleiraRepository repository;

    @Override
    public List<PrateleiraEntity> listarPrateleirasDisponiveis() {
        return repository.findByDisponivelTrue();
    }

    @Override
    public PrateleiraEntity alocarPrateleiraParaProducao(int prateleiraId) throws Exception {
        Optional<PrateleiraEntity> prateleiraOpt = repository.findById(prateleiraId);

        if (prateleiraOpt.isPresent()) {
            PrateleiraEntity prateleira = prateleiraOpt.get();
            if (prateleira.getDisponivel()) {
                prateleira.setDisponivel(false);
                return repository.save(prateleira);
            } else {
                throw new Exception("A prateleira escolhida não está disponível.");
            }
        } else {
            throw new Exception("Prateleira não encontrada.");
        }

    }

    @Override
    public void liberarPrateleira(int prateleiraId) {
        Optional<PrateleiraEntity> prateleiraOpt = repository.findById(prateleiraId);
        if (prateleiraOpt.isPresent()) {
            PrateleiraEntity prateleira = prateleiraOpt.get();
            prateleira.setDisponivel(true);
            repository.save(prateleira);
        }
    }

    public List<PrateleiraEntity> listar(){
        return repository.findAll();
    }
}
