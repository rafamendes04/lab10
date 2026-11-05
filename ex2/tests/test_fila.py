import pytest
from fila import Fila

def test_fila_nova():
    assert Fila().aguardando == 0

def test_emitir_normal():
    assert Fila().emitir("normal") == "N1"

def test_duas_normais():
    f = Fila()
    assert f.emitir("normal") == "N1"
    assert f.emitir("normal") == "N2"

def test_emitir_prioritaria():
    assert Fila().emitir("prioritaria") == "P1"

def test_numeracao_por_tipo():
    f = Fila()
    assert f.emitir("normal") == "N1"
    assert f.emitir("prioritaria") == "P1"
    assert f.emitir("normal") == "N2"

def test_tipo_invalido():
    with pytest.raises(ValueError):
        Fila().emitir("vip")

def test_aguardando():
    f = Fila()
    f.emitir("normal")
    f.emitir("prioritaria")
    assert f.aguardando == 2

def test_chamar_fila_vazia():
    with pytest.raises(IndexError):
        Fila().chamar()

def test_chamar_devolve_senha():
    f = Fila()
    f.emitir("normal")
    assert f.chamar() == "N1"

def test_chamar_reduz_aguardando():
    f = Fila()
    f.emitir("normal")
    f.emitir("normal")
    f.chamar()
    assert f.aguardando == 1

def test_normais_em_ordem_de_chegada():
    f = Fila()
    f.emitir("normal")
    f.emitir("normal")
    assert f.chamar() == "N1"
    assert f.chamar() == "N2"

def test_prioritaria_passa_na_frente():
    f = Fila()
    f.emitir("normal")
    f.emitir("prioritaria")
    assert f.chamar() == "P1"

def test_prioritarias_em_ordem_de_chegada():
    f = Fila()
    f.emitir("prioritaria")
    f.emitir("prioritaria")
    assert f.chamar() == "P1"
    assert f.chamar() == "P2"

def test_depois_de_duas_prioritarias_vem_normal():
    f = Fila()
    f.emitir("normal")
    for _ in range(3):
        f.emitir("prioritaria")
    assert f.chamar() == "P1"
    assert f.chamar() == "P2"
    assert f.chamar() == "N1"
