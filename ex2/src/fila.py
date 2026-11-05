class Fila:
    def __init__(self):
        self.n = 0

    def emitir(self, tipo):
        self.n += 1
        return "N" + str(self.n)

    @property
    def aguardando(self):
        return 0
