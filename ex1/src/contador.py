def contar_palavras(texto):
    resultado = {}
    for p in texto.split():
        resultado[p] = resultado.get(p, 0) + 1
    return resultado
