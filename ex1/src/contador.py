def contar_palavras(texto):
    resultado = {}
    for p in texto.lower().split():
        resultado[p] = resultado.get(p, 0) + 1
    return resultado
