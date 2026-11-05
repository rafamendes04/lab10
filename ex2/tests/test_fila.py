import pytest
from fila import Fila

def test_fila_nova():
    assert Fila().aguardando == 0
