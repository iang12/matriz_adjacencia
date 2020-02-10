"""Implemente uma função que gere a matriz de adjacência de um grafo. Para
isso, utilize a biblioteca Networkx em Python como base para realizar essa
atividade de implementação."""

#alunos VINICIUS,IAN

import networkx 
import matplotlib.pyplot as plt #plotar o grafo

arestas = [(1,2), (1,3), (2,3), (2,4), (3,4)]
G       = networkx.Graph(arestas)

def gerar_matriz(graph):
    matriz = []

    for i in graph.nodes():
        #print(graph.nodes(),'n1')
        matriz.append([])
        for j in graph.nodes():
            matriz[i - 1].append(0)

    for i in graph.nodes():    
        for j in graph.neighbors(i):
            matriz[i - 1][j - 1] = 1

    return matriz
print('MATRIZ GERADA')
print(gerar_matriz(G))#mostra a matriz
networkx.draw(G) #plotar o grafo
plt.show() #plotar o grafo