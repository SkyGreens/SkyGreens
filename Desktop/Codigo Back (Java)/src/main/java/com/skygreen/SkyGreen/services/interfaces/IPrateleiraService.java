package com.skygreen.SkyGreen.services.interfaces;

import java.util.List;

import com.skygreen.SkyGreen.entities.PrateleiraEntity;

public interface IPrateleiraService {

    List<PrateleiraEntity> listarPrateleirasDisponiveis();
    
    PrateleiraEntity alocarPrateleiraParaProducao(int prateleiraId) throws Exception;

    void liberarPrateleira(int prateleiraId);

}