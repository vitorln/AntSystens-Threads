# -*- coding: utf-8 -*

class Formiga:
    def __init__(self): #construtor da formiga
        self.pos = -1 #posiçao atual da formiga
        self.caminho = [] #caminho q a formiga percorreu
        self.distancia = 0.0 #distancia q a formiga percorreu

    def atualizaDistancia(self, valor): #atualiza a distancia q a formiga percorreu depois q ela mudar de cidade 
        self.distancia += valor

    def atualizaCaminho(self, cidade): #atualiza o caminho q a formiga percorreu quando a formiga mudar de cidade
        self.caminho.append(cidade)

    def setPosicao(self, pos): #atualiza a posiçao atual da formiga
        self.pos = pos

    def getDistancia(self): #retorna distancia
        return self.distancia

    def getCaminho(self): #retorna o caminho
        return self.caminho

    def getPos(self): #retorna a posiçao atual
        return self.pos

    def printCaminho(self):
        for i, cidade in enumerate(self.caminho):
            print("cidade ", i, ": ", cidade)

        print("\n distancia final: ",self.distancia) 