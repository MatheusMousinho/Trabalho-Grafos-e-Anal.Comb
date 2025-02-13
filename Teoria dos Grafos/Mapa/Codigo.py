
# Auxilia a encontrar o líder de um conjunto
def Encontrar(conjuntos, cidade):
    if (conjuntos[cidade] != cidade):
        conjuntos[cidade] = Encontrar(conjuntos, conjuntos[cidade])
    return conjuntos[cidade]

#Uni dois conjuntos
def Unir(conjuntos, tier, nodo1, nodo2):
    raiz1 = Encontrar(conjuntos, nodo1)
    raiz2 = Encontrar(conjuntos, nodo2)
    Ranquear(raiz1, raiz2, tier, conjuntos)
    
#Decide como uni dois conjuntos
def Ranquear(raiz1, raiz2, tier, conjuntos):    
    if (raiz1 != raiz2):
        if (tier[raiz1] > tier[raiz2]):
            conjuntos[raiz2] = raiz1
        elif (tier[raiz1] < tier[raiz2]):
            conjuntos[raiz1] = raiz2
        elif (tier[raiz1] == tier[raiz2]):
            conjuntos[raiz2] = raiz1
            tier[raiz1] += 1


def kruskal(arestas):
    resultado = 0
    for Nodo, Vizinho, peso in arestas:
        if (Encontrar(conjuntos, Nodo) != Encontrar(conjuntos, Vizinho)):
            Unir(conjuntos, tier, Nodo, Vizinho)
            resultado += peso
    
    print(resultado) 



n, m = map(int, input().split()) 
conjuntos = list(range(n))
tier = [0] * n
arestas = []
for i in range (m):
    v1, v2, peso = map(int, input().split())
    arestas.append((v1 - 1, v2 - 1, peso))  

arestas.sort(key=lambda x: x[2])

kruskal(arestas)
