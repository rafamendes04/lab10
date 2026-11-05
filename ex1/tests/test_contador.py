from contador import contar_palavras

def test_vazio():
    assert contar_palavras("") == {}

def test_uma_palavra():
    assert contar_palavras("teste") == {"teste": 1}

def test_duas_palavras():
    assert contar_palavras("bom dia") == {"bom": 1, "dia": 1}
