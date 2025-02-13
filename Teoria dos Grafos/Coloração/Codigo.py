def contar_cliques(n, m, imagem, cores):
    
    for linha in range(n):
        for coluna in range(m):
            if (imagem[linha][coluna] == '.' and (visitado[linha][coluna] == 0)):
                visitado[linha][coluna] = 1
                cores += 1
                pilha = [(linha, coluna)]
                while pilha:
                    linha_atual, coluna_atual = pilha.pop()
                    for deslocamento_x, deslocamento_y in movimentos:
                        nova_linha = linha_atual + deslocamento_x
                        nova_coluna = coluna_atual + deslocamento_y
                        if 0 <= nova_linha < n and 0 <= nova_coluna < m and not visitado[nova_linha][nova_coluna] and imagem[nova_linha][nova_coluna] == '.':
                            visitado[nova_linha][nova_coluna] = True
                            pilha.append((nova_linha, nova_coluna))
    
    return cores
  


n, m = map(int, input().split())
imagem = [input().strip() for i in range(n)]
visitado = [[0] * m for _ in range(n)]
movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cores = 0
print(contar_cliques(n, m, imagem, cores))
