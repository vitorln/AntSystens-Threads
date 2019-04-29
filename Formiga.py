class Formiga:
    def __init__(self):
        self.pos = -1
        self.caminho = []
        self.distancia = 0.0

    def atualizaDistancia(self, valor):
        self.distancia += valor

    def atualizaCaminho(self, cidade):
        self.caminho.append(cidade)

    def setPosicao(self, pos):
        self.pos = pos

    def getDistancia(self)
    def getCaminho(self)
    def getPos(self)
