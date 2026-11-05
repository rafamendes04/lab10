import pytest
from fila import Fila

def test_fila_nova():
    assert Fila().aguardando == 0

def test_emitir_normal():
    assert Fila().emitir("normal") == "N1"
