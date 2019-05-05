# -*- coding: utf-8 -*
import threading
from Formiga import Formiga
from Cidades import Cidades
import random
import time


def readFile(name, cidades): 
    with open("dados/" + name + ".txt", "r") as file:
        data = file.read() #le o arquivo de com as cidades
    lines = data.split('\n') #cria um vetor de cidades 
    for line in lines:
        coordinates = line.split(" ") # para cada cidade, cria um vetor de coordenadas
        cidades.setCidades(float(coordinates[0]), float(coordinates[1])) #parametros: coordenada X e Y de uma cidade
        
def AS(cidades):
    global cont 
    global melhor_formiga
    melhor_formiga = Formiga() #chama o construtos de formiga
    #cria uma "melhor formiga", com um caminho linear e sua respectiva distancia, para servir de comparaçao para as demais
    for i in range(cidades.getSize() - 1):
        melhor_formiga.atualizaCaminho(i)
        melhor_formiga.atualizaDistancia(cidades.getDistancia(i, i+1))
    melhor_formiga.atualizaCaminho(cidades.getSize() - 1)
    melhor_formiga.atualizaDistancia(cidades.getDistancia(cidades.getSize() - 1, 0))

    for i in range(cidades.getSize() * 10): #"for" de geraçoes de formigas
    #for i in range(10):
        threads = [] #cria vetor de threads
        cont = 0
        for j in range(cidades.getSize()): # "for" de formigas
        #for j in range(1):
            formiga = Formiga() #cria uma formiga
            formiga.setPosicao(j) #seta uma posiçao inicial, cada formiga inicia em uma cidade  
            formiga.atualizaCaminho(j) #seta a primeira cidade do caminho percorrido
            t = threading.Thread(target=executa, args=(formiga, cidades, cidades.getSize())) # cria a thread na funçao "executa"
            t.daemon = True #faz com q a thread morra quando o pai morrer
            t.start() #inicia a thread
            threads.append(t) #acrecenta a thread em um vetor de threads

        for thread in threads:
            thread.join() #espera todas as threads terminarem    
    
    melhor_formiga.printCaminho()
    
            


def executa(formiga, cidades, tam, ):
    global mutex1
    global espera
    global cont
    global melhor_formiga
    for i in range(cidades.getSize()):
        probabilidade = calcProb(formiga, cidades) #calcula a probabilidade de uma formiga ir para alguma cidade, retorna um vetor de probabilidades
        indice = roleta(probabilidade)
        formiga.setPosicao(indice)
        formiga.atualizaCaminho(indice)
        formiga.atualizaDistancia(cidades.getDistancia(formiga.getCaminho()[-1],formiga.getCaminho()[-2]))

    formiga.atualizaDistancia(cidades.getDistancia(formiga.getCaminho()[0],formiga.getCaminho()[-1]))
    #primeira condição de disputa: todas as formigas tem de ter terminado suas rootas para poder atualizar os feromonios
    #bloco de espera
    espera.acquire()
    cont +=1
    if cont == tam:
        cidades.evaporaFeromnonio() # esta aqui para garanti q evapore apenas uma vez
        espera.notifyAll()
        espera.release()
    else:
        espera.wait()
        espera.release()
    #fim do bloco de espera
    
    atualizaFeromonio(cidades, formiga) #atualisa feromonios, é onde esta a segunda condição de disputa

    mutex1.acquire() #terceira condição de disputa: uma formiga de cada vez tem de verificar se percorreu o menor cominho
    if melhor_formiga.getDistancia() > formiga.getDistancia():
        melhor_formiga = formiga 
    mutex1.release()        

def calcProb(formiga, cidades):
    probability = []    #cria vetor de probabilidades
    #calcula a probabilidade de uma formiga ir para cada uma das cidades
    for i in range(cidades.getSize()):
        if i in formiga.getCaminho(): #verifica se a formiga ja passou pela cidade
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

def roleta(probabilidade):
    sorteado = random.random()* probabilidade[-1]
    for i, prob in enumerate(probabilidade):
        if sorteado <= prob:
            return i

def atualizaFeromonio(cidades, formiga):
    global mutex
    for i in range(cidades.getSize()):
        for j in range(cidades.getSize()):
            for k in range(cidades.getSize()):
                if (formiga.caminho[k] == i) and (formiga.caminho[k-1] == j):
                    mutex.acquire() #segunda condição de disputa: uma formiga de cada vez deve atualizar os feromonios na tabela
                    cidades.depositaFeromnonio(formiga.caminho[k], formiga.caminho[k-1], 1.0/formiga.getDistancia())
                    mutex.release()
                    break
                elif (formiga.caminho[k] == j) and (formiga.caminho[k-1] == i):
                    mutex.acquire() #segunda condição de disputa: uma formiga de cada vez deve atualizar os feromonios na tabela
                    cidades.depositaFeromnonio(formiga.caminho[k], formiga.caminho[k-1], 1.0/formiga.getDistancia())
                    mutex.release()
                    break

def main():
    
    cidades = Cidades() #chamada de construtor de Cidades

    #abre o arquivo da base da dados
    readFile("att48", cidades) #parametros: nome da base e objeto cidades
    global mutex
    mutex  = threading.Semaphore(1)
    global mutex1
    mutex1  = threading.Semaphore(1)
    global espera
    espera  = threading.Condition()
    global cont 
    cidades.geraMatrizes() #gera matrizes de distancia e feromonios
    
    AS(cidades) #inicia a função do AntSystens

if __name__ == "__main__":
    start_time = time.time() 
    main()
    print("--- %s seconds ---" % (time.time() - start_time))