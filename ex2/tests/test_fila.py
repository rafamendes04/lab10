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
