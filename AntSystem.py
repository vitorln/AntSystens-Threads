import threading
from Formiga import Formiga
from Cidades import Cidades

def readFile(name, cidades):
    with open("dados/" + name + ".txt", "r") as file:
        data = file.read()
    lines = data.split('\n')
    for i, line in enumerate(lines):
        coordinates = line.split(" ")
        cidades.setCidades(float(coordinates[0]),float(coordinates[1]))
        
def AS(cidades):
    melhor_formiga = Formiga()

    for i in range(cidades.getSize() - 1):
        melhor_formiga.atualizaCaminho(i)
        melhor_formiga.atualizaDistancia(cidades.getDistancia(i, i+1))
    melhor_formiga.atualizaCaminho(cidades.getSize() - 1)
    melhor_formiga.atualizaDistancia(cidades.getDistancia(cidades.getSize() - 1, 0))

    for i in range(cidades.getSize() * 10):
        for j in range(cidades.getSize()):
            formiga = Formiga()
            formiga.setPosicao(j)
            formiga.atualizaCaminho(j)
            t = threading.Thread(target=executa, args(formiga, cidades))

def executa(formiga, cidades):
    for i in range(cidades.getSize()):

def calcProb(formiga, ):         



def main():
    #parametros: nome da base
    cidades = Cidades()

    readFile("att48", cidades)
    cidades.geraMatrizes()

if __name__ == "__main__":
    main()


