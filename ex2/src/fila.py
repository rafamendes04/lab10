class Fila:
    def __init__(self):
        self.n = 0
        self.p = 0

    def emitir(self, tipo):
        if tipo == "prioritaria":
            self.p += 1
            return "P" + str(self.p)
        self.n += 1
        return "N" + str(self.n)

    @property
    def aguardando(self):
        return 0
