from contador import contar_palavras

def test_vazio():
    assert contar_palavras("") == {}
