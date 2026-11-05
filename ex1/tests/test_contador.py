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

def test_maiusculas():
    assert contar_palavras("Dia dia DIA") == {"dia": 3}

def test_ponto_e_exclamacao():
    assert contar_palavras("fim. Fim!") == {"fim": 2}

def test_virgula_e_ponto_virgula():
    assert contar_palavras(",dia, ;dia;") == {"dia": 2}

def test_dois_pontos_e_interrogacao():
    assert contar_palavras(":dia: ?dia?") == {"dia": 2}

def test_so_sinais():
    assert contar_palavras("... !") == {}
