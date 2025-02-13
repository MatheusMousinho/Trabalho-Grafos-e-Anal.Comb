#include <stdio.h>
#include <string.h>
#define INF 0x3f3f3f3f
#define MAXN 251
#define MAXM 31125

int distancias[MAXN];
int adj[MAXN][MAXN];
int visitados[MAXN];
int numVertices, numArestas, destino, origem;

int distanciaMinima() {
    int min = INF, indiceMin = -1;

    for (int v = 0; v < numVertices; v++) {
        if (!visitados[v] && distancias[v] < min) {
            min = distancias[v];
            indiceMin = v;
        }
    }
    return indiceMin;
}

int dijkstra() {
    for (int i = 0; i < numVertices; i++) {
        distancias[i] = INF;
        visitados[i] = 0;
    }

    distancias[origem] = 0;

    for (int count = 0; count < numVertices-1; count++) {
        int u = distanciaMinima();
        if (u == -1) break;
        visitados[u] = 1;

        for (int v = 0; v < numVertices; v++) {
            if (!visitados[v] && adj[u][v] != INF) {
                if (u < destino) {
                    if (v == u + 1) {
                        if (distancias[u] + adj[u][v] < distancias[v]) {
                            distancias[v] = distancias[u] + adj[u][v];
                        }
                    }
                } else {
                    if (v < destino) {
                        if (distancias[u] + adj[u][v] < distancias[v]) {
                            distancias[v] = distancias[u] + adj[u][v];
                        }
                    } else {
                        if (distancias[u] + adj[u][v] < distancias[v]) {
                            distancias[v] = distancias[u] + adj[u][v];
                        }
                    }
                }
            }
        }
    }

    return distancias[destino - 1];
}

int main() {
    while (1) {
        scanf("%d %d %d %d", &numVertices, &numArestas, &destino, &origem);
        if (numVertices == 0 && numArestas == 0 && destino == 0 && origem == 0) break;

        for (int i = 0; i < numVertices; i++) {
            for (int j = 0; j < numVertices; j++) {
                adj[i][j] = INF;
            }
            adj[i][i] = 0;
        }

        for (int i = 0; i < numArestas; i++) {
            int u, v, p;
            scanf("%d %d %d", &u, &v, &p);
            adj[u][v] = adj[v][u] = p;
        }

        printf("%d\n", dijkstra());
    }

    return 0;
