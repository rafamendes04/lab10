from contador import contar_palavras

def test_vazio():
    assert contar_palavras("") == {}

def test_uma_palavra():
    assert contar_palavras("teste") == {"teste": 1}

def test_duas_palavras():
    assert contar_palavras("bom dia") == {"bom": 1, "dia": 1}

def test_quebra_de_linha():
    assert contar_palavras("bom\ndia") == {"bom": 1, "dia": 1}

def test_varios_espacos():
    assert contar_palavras("bom   dia") == {"bom": 1, "dia": 1}

def test_hifen():
    assert contar_palavras("guarda-chuva") == {"guarda-chuva": 1}

def test_palavra_repetida():
    assert contar_palavras("dia a dia") == {"dia": 2, "a": 1}
