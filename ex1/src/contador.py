def contar_palavras(texto):
    resultado = {}
    for p in texto.split():
        resultado[p] = 1
    return resultado
