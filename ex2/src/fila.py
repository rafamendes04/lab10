class Fila:
    def __init__(self):
        self.n = 0
        self.p = 0
        self.normais = []
        self.prios = []
        self.seguidas = 0

    def emitir(self, tipo):
        if tipo not in ("normal", "prioritaria"):
            raise ValueError
        if tipo == "prioritaria":
            self.p += 1
            senha = "P" + str(self.p)
            self.prios.append(senha)
        else:
            self.n += 1
            senha = "N" + str(self.n)
            self.normais.append(senha)
        return senha

    def chamar(self):
        if self.prios and self.seguidas < 2:
            self.seguidas += 1
            return self.prios.pop(0)
        return self.normais.pop(0)

    @property
    def aguardando(self):
        return len(self.normais) + len(self.prios)
