import threading
from Formiga import Formiga
from Cidades import Cidades

def readFile(name, cidades): 
    with open("dados/" + name + ".txt", "r") as file:
        data = file.read() #le o arquivo de com as cidades
    lines = data.split('\n') #cria um vetor de cidades 
    for line in enumerate(lines):
        coordinates = line.split(" ") # para cada cidade, cria um vetor de coordenadas
        cidades.setCidades(float(coordinates[0]),float(coordinates[1])) #parametros: coordenada X e Y de uma cidade
        
def AS(cidades):
    melhor_formiga = Formiga() #chama o construtos de formiga
    #cria uma "melhor formiga", com um caminho linear e sua respectiva distancia, para servir de comparaçao para as demais
    for i in range(cidades.getSize() - 1):
        melhor_formiga.atualizaCaminho(i)
        melhor_formiga.atualizaDistancia(cidades.getDistancia(i, i+1))
    melhor_formiga.atualizaCaminho(cidades.getSize() - 1)
    melhor_formiga.atualizaDistancia(cidades.getDistancia(cidades.getSize() - 1, 0))

    for i in range(cidades.getSize() * 10): #"for" de geraçoes de formigas
        threads = [] #cria vetor de threads
        for j in range(cidades.getSize()): # "for" de formigas
            formiga = Formiga() #cria uma formiga
            formiga.setPosicao(j) #seta uma posiçao inicial, cada formiga inicia em uma cidade  
            formiga.atualizaCaminho(j) #seta a primeira cidade do caminho percorrido
            t = threading.Thread(target=executa, args(formiga, cidades)) # cria a thread na funçao "executa"
            t.daemon = True #faz com q a thread morra quando o pai morrer
            t.start() #inicia a thread
           	threads.append(t) #acrecenta a thread em um vetor de threads

	        for thread in threads:
		        thread.join() #espera todas as threads terminarem
	        
            


def executa(formiga, cidades):
    for i in range(cidades.getSize()):
        probabilidade = calcProb(formiga, cidades) #calcula a probabilidade de uma formiga ir para alguma cidade, retorna um vetor de probabilidades

def calcProb(formiga, cidades):
    probability = []    #cria vetor de probabilidades
    #calcula a probabilidade de uma formiga ir para cada uma das cidades
    for i in range(cidades.getSize()):
        if i in formiga.gettCaminho: #verifica se a formiga ja passou pela cidade
            probability.append(0) #seta a probabilidade como 0 se a formiga ja passou pela cidade
        else:
            aux=0
            if cidades.getDistancia(formiga.getPos(), i) != 0: #previne erro de divisao por 0
                aux = 1/cidades.getDistancia(formiga.getPos(), i)
            probability.append((cidades.getFeromonio(formiga.getPos(), i) ** 2) * aux) #calcula probabilidade e salva no vetor de probabilidades
    #calcula da probabilidade acumulada
    for i in range(cidades.getSize()-1):
        probability[i+1]+=probability[i] #acumula as probabilidades para facilitar na roleta

    return probability #retorna vetor de probabilidades

def main():
    
    cidades = Cidades() #chamada de construtor de Cidades
    
    #abre o arquivo da base da dados
    readFile("att48", cidades) #parametros: nome da base e objeto cidades

    cidades.geraMatrizes() #gera matrizes de distancia e feromonios
    
    AS(cidades) #inicia a função do AntSystens

if __name__ == "__main__":
    main()