import math

class Cidades:

    def __init__(self):
        self.cidades = []
        self.matriz_dist = []
        self.matriz_feromonios = []
        
    def setCidades(self, x, y):
        self.cidades.append((x, y))

    def printCidades(self):
        print(self.cidades)

    def printMatrizDist(self):
        print(self.matriz_dist)
        print(self.matriz_feromonios)
        
    def geraMatrizes(self):
        qtd = len(self.cidades)
        for i in range(qtd):
            aux, aux2 = [], []
            for j in range(qtd):
                aux.append(math.sqrt((self.cidades[i][0] - self.cidades[j][0])**2 + (self.cidades[i][1] - self.cidades[j][1])**2))
                aux2.append(1)
            self.matriz_dist.append(aux)
            self.matriz_feromonios.append(aux2)
    
    def getSize(self):
        return len(self.cidades)]
    
    def getDistancia(self, x, y):
        return matriz_dist[x][y]


    




