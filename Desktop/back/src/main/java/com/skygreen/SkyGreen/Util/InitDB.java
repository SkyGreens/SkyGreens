package com.skygreen.SkyGreen.Util;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

import com.skygreen.SkyGreen.Controller.AuthenticationController;
import com.skygreen.SkyGreen.DTO.RegisterDTO;
import com.skygreen.SkyGreen.entities.ClienteEntity;
import com.skygreen.SkyGreen.entities.FornecedorEntity;
import com.skygreen.SkyGreen.entities.PedidoCompraEntity;
import com.skygreen.SkyGreen.entities.PedidoVendaEntity;
import com.skygreen.SkyGreen.entities.PrateleiraEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.entities.UsuarioRole;
import com.skygreen.SkyGreen.repositories.ClienteRepository;
import com.skygreen.SkyGreen.repositories.FornecedorRepository;
import com.skygreen.SkyGreen.repositories.PedidoCompraRepository;
import com.skygreen.SkyGreen.repositories.PedidoVendaRepository;
import com.skygreen.SkyGreen.repositories.PrateleiraRepository;
import com.skygreen.SkyGreen.repositories.SementeRepository;
import com.skygreen.SkyGreen.services.ClienteServiceImpl;
import com.skygreen.SkyGreen.services.FornecedorServiceImpl;
import com.skygreen.SkyGreen.services.PedidoCompraServiceImpl;
import com.skygreen.SkyGreen.services.PedidoVendaServiceImpl;
import com.skygreen.SkyGreen.services.SementeServiceImpl;

@Component
@Profile("dsv")
public class InitDB implements CommandLineRunner {
    
    @Autowired
    AuthenticationController authenticationController;
    
    @Autowired
    private PrateleiraRepository prateleiraRepository;
    
    @Autowired
    private SementeRepository sementeRepository;

    @Autowired
    private SementeServiceImpl sementeService;

    @Autowired
    private FornecedorServiceImpl fornecedorService;

    @Autowired
    private FornecedorRepository fornecedorRepository;

    @Autowired
    private PedidoCompraServiceImpl pedidoCompraService;

    @Autowired
    private PedidoCompraRepository pedidoCompraRepository;

    @Autowired
    private ClienteServiceImpl clienteService;

    @Autowired
    private ClienteRepository clienteRepository;

    @Autowired
    private PedidoVendaServiceImpl pedidoVendaService;

    @Autowired
    private PedidoVendaRepository pedidoVendaRepository;

    public void inserindoRegistro() throws Exception {
        System.out.println("Inserindo registros");

        //Usuario

        RegisterDTO admin = new RegisterDTO("12345678909", "admin", UsuarioRole.ADMIN,
                "admin@skygreen.com", true, "Admin");
        authenticationController.register(admin);

        RegisterDTO gerente = new RegisterDTO("45242561807", "gerente", UsuarioRole.GERENTEPRODUCAO,
                "gerenteproducao@skygreen.com", true, "Gerente Produção");
        authenticationController.register(gerente);

        RegisterDTO assistente = new RegisterDTO("01800980809", "assistente", UsuarioRole.ASSISTENTEPRODUCAO,
                "assistenteproducao@skygreen.com", true, "Assistente Produção");
        authenticationController.register(assistente);

        //Prateleiras

        if (prateleiraRepository.count() == 0) {
            prateleiraRepository.save(new PrateleiraEntity("Prateleira 1", true));
            prateleiraRepository.save(new PrateleiraEntity("Prateleira 2", true));
            prateleiraRepository.save(new PrateleiraEntity("Prateleira 3", true));
            prateleiraRepository.save(new PrateleiraEntity("Prateleira 4", true));
        }

        //Semente
        
        SementeEntity semente = new SementeEntity();

        semente.setNome("Hortelã");
        semente.setDescricao("verdinho");  

        
        semente = sementeService.criarSemente(semente);

        sementeRepository.save(semente);

        //Fornecedor

        FornecedorEntity fornecedor = new FornecedorEntity();

        fornecedor.setAtivo(true);
        fornecedor.setCidade("Jacarei");
        fornecedor.setCnpj("0310608200303");
        fornecedor.setEmail("fornecedor@gmail.com");
        fornecedor.setEndereco("Rua santa cruz");
        fornecedor.setInscricaoEstadual(123456789);
        fornecedor.setTelefone("12988888888");
        fornecedor.setEstado("SP");
        fornecedor.setFornecedorId(0);
        List<SementeEntity> idSemente = sementeRepository.findAllById(List.of(1));
        fornecedor.setSementes(idSemente);
        fornecedor.setPais("Brasil");
        fornecedor.setRazaoSocial("Hortelã primes");

        fornecedor = fornecedorService.add(fornecedor);
        fornecedorRepository.save(fornecedor);

        //Pedido Compra

        PedidoCompraEntity pedidoCompra = new PedidoCompraEntity();

        pedidoCompra.setFornecedor(fornecedor);
        pedidoCompra.setQuantidade(100);
        pedidoCompra.setSemente(semente);

        pedidoCompra = pedidoCompraService.criarPedido(pedidoCompra);
        pedidoCompraRepository.save(pedidoCompra);

        //Cliente

        ClienteEntity cliente = new ClienteEntity();

        cliente.setAtivo(true);
        cliente.setCidade("Jacarei");
        cliente.setClienteId(0);
        cliente.setCnpj("50715875000303");
        cliente.setEmail("cliente@gmail.com");
        cliente.setEndereco("Rua Goias");
        cliente.setEstado("SP");
        cliente.setPais("Brasil");
        cliente.setRazaoSocial("Fazenda do tigrinho");
        cliente.setTelefone("12966666666");

        cliente = clienteService.add(cliente);
        clienteRepository.save(cliente);

        //Pedido venda

        PedidoVendaEntity pedidoVenda = new PedidoVendaEntity();

        pedidoVenda.setAtivo(true);
        pedidoVenda.setCliente(cliente);
        pedidoVenda.setPedidoVendaId(0);
        pedidoVenda.setQuantidade(50);
        pedidoVenda.setSemente(semente);
        pedidoVenda.setTempoCultivo(10);

        pedidoVenda = pedidoVendaService.criarVenda(pedidoVenda);
        pedidoVendaRepository.save(pedidoVenda);


    }

    @Override
    public void run(String... args) throws Exception {
        inserindoRegistro();
    }
}
