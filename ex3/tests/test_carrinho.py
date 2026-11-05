from carrinho import Carrinho
import pytest

def test_carrinho_vazio():
    assert Carrinho().total == 0

def test_um_item():
    c = Carrinho()
    c.adicionar(2500)
    assert c.total == 2500

def test_item_com_quantidade():
    c = Carrinho()
    c.adicionar(2500, quantidade=2)
    assert c.total == 5000

def test_preco_zero_rejeitado():
    with pytest.raises(ValueError):
        Carrinho().adicionar(0)

def test_cupom_dez():
    c = Carrinho()
    c.adicionar(5000)
    c.aplicar_cupom("DEZ")
    assert c.total == 4500

def test_cupom_desconhecido():
    with pytest.raises(ValueError):
        Carrinho().aplicar_cupom("XYZ")

def test_item_depois_do_cupom():
    c = Carrinho()
    c.aplicar_cupom("DEZ")
    c.adicionar(1000)
    assert c.total == 900
