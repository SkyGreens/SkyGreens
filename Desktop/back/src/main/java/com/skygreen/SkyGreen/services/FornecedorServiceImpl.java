package com.skygreen.SkyGreen.services;

import java.util.List;
import java.util.ArrayList;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;

import com.skygreen.SkyGreen.entities.FornecedorEntity;
import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.repositories.FornecedorRepository;
import com.skygreen.SkyGreen.repositories.SementeRepository;
import com.skygreen.SkyGreen.services.interfaces.IFornecedorService;

@Service
public class FornecedorServiceImpl implements IFornecedorService {

    @Autowired
    private FornecedorRepository repository;

    @Autowired
    private SementeRepository sementeRepository;

    @Override
    public List<FornecedorEntity> findAll() {
        return repository.findAll();
    }

    @Override
    public FornecedorEntity add(FornecedorEntity fornecedor) {
        if (fornecedor.getSementes() != null && !fornecedor.getSementes().isEmpty()) {
            List<SementeEntity> sementesAssociadas = new ArrayList<>();

            for (SementeEntity semente : fornecedor.getSementes()) {
                SementeEntity sementeExistente = sementeRepository.findById(semente.getSementeId())
                        .orElseThrow(() -> new RuntimeException(
                                "Semente não encontrada com id: " + semente.getSementeId()));

                sementeExistente.setFornecedor(fornecedor);
                sementesAssociadas.add(sementeExistente);
            }

            fornecedor.setSementes(sementesAssociadas);
        } else {
            fornecedor.setSementes(null);

        }

        fornecedor = repository.save(fornecedor);
        return fornecedor;
    }

    @Override
    public Optional<FornecedorEntity> findById(Integer id) {
        return repository.findById(id);
    }

    @Override
    public void delete(Integer id) {
        repository.deleteById(id);
    }

    @Override
    public FornecedorEntity update(@RequestBody FornecedorEntity fornecedor) {
        fornecedor = repository.save(fornecedor);
        return fornecedor;
    }

    @Override
    public FornecedorEntity updateSementes(@PathVariable Integer fornecedorId,
            @RequestBody List<SementeEntity> sementes) {

        FornecedorEntity fornecedorExistente = repository.findById(fornecedorId)
                .orElseThrow(() -> new RuntimeException("Fornecedor não encontrado com ID: " + fornecedorId));

        List<SementeEntity> sementeExistente = new ArrayList<>();
        for (SementeEntity semente : sementes) {

            SementeEntity sementeId = sementeRepository.findById(semente.getSementeId())
                    .orElseThrow(() -> new RuntimeException(
                            "Semente não encontrada com ID: " + semente.getSementeId()));

            if (sementeId.getFornecedor() == null
                    || !sementeId.getFornecedor().getFornecedorId().equals(fornecedorExistente.getFornecedorId())) {
                sementeId.setFornecedor(fornecedorExistente);
                sementeExistente.add(sementeId);
            } else {
                throw new IllegalArgumentException(
                        "Semente com ID " + sementeId.getSementeId() + " já está vinculada ao fornecedor.");
            }
        }

        fornecedorExistente.setSementes(sementeExistente);

        return repository.save(fornecedorExistente);
    }

}
