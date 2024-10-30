package com.skygreen.SkyGreen.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.skygreen.SkyGreen.entities.PedidoVendaEntity;
import com.skygreen.SkyGreen.services.interfaces.IPedidoVendaService;

@RestController
@RequestMapping("/vendas")
public class PedidoVendasController {

    @Autowired
    private IPedidoVendaService pedidoVendaService;

    @PostMapping("/pedido")
    public PedidoVendaEntity criarVenda(@RequestBody PedidoVendaEntity pedidoVenda) throws Exception {
        return pedidoVendaService.criarVenda(pedidoVenda);
    }

    @GetMapping("/listar")
    public List<PedidoVendaEntity> getVenda() {
        return pedidoVendaService.getVenda();
    }
}
