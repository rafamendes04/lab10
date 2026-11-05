def contar_palavras(texto):
    resultado = {}
    for p in texto.lower().split():
        p = p.strip(".,;:!?")
        resultado[p] = resultado.get(p, 0) + 1
    return resultado
