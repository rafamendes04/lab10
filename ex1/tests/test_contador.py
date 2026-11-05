from contador import contar_palavras

def test_vazio():
    assert contar_palavras("") == {}

def test_uma_palavra():
    assert contar_palavras("teste") == {"teste": 1}
