class Fila:
    def __init__(self):
        self.n = 0
        self.p = 0
        self.senhas = []

    def emitir(self, tipo):
        if tipo not in ("normal", "prioritaria"):
            raise ValueError
        if tipo == "prioritaria":
            self.p += 1
            senha = "P" + str(self.p)
        else:
            self.n += 1
            senha = "N" + str(self.n)
        self.senhas.append(senha)
        return senha

    @property
    def aguardando(self):
        return len(self.senhas)
