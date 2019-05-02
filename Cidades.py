import math

class Cidades:

    
    def __init__(self): #construtos de Cidades
        self.cidades = [] #vetor com todas as cidades
        self.matriz_dist = [] #matriz com as distancias emtre as cidades
        self.matriz_feromonios = [] #matriz com os feromonios entre as cidades
        
    def setCidades(self, x, y): #adciona uma nova cidade no vertor de cidades
        self.cidades.append((x, y)) #cada cidade tem uma tupla com as coordenadas X e Y

    def printCidades(self): #printa vetor de cidades
        print(self.cidades)

    def printMatrizDistancia(self): #printa vetor de cidades
        print(self.matriz_dist)

    def printMatrizFeromonios(self): #printa vetor de cidades
        print(self.matriz_feromonios)
        
    def geraMatrizes(self): #calcula a distancia euclidiana entre cada cidade e iniciliza os feromonios com 1
        qtd = len(self.cidades)
        for i in range(qtd):
            aux, aux2 = [], []
            for j in range(qtd):
                aux.append(math.sqrt((self.cidades[i][0] - self.cidades[j][0])**2 + (self.cidades[i][1] - self.cidades[j][1])**2))
                aux2.append(1)
            self.matriz_dist.append(aux)
            self.matriz_feromonios.append(aux2)
    
    def getSize(self): #retorna a quantidade de cidades
        return len(self.cidades)]
    
    def getDistancia(self, x, y): #retorna a distancia entre a as cidades X e Y
        return matriz_dist[x][y]

    def getFeromonio(self, x, y): #retorna os feromonios entre a cidade X e Y
        return matriz_feromonios[x][y]
