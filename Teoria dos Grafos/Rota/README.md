O sistema rodoviário de um país interliga todas as suas N cidades de modo que, a partir de uma cidade qualquer, é possível chegar a cada uma das outras cidades trafegando pelas estradas existentes. Cada estrada liga duas cidades distintas, tem mão dupla e um único posto de pedágio (o pedágio é pago nos dois sentidos de tráfego). As estradas não se intersectam a não ser nas cidades. Nenhum par de cidades é interligado por duas ou mais estradas.

A Transportadora Dias oferece um serviço de transporte de encomendas entre as cidades. Cada encomenda deve ser levada de uma cidade A para uma outra cidade B. A direção da Transportadora Dias define, para cada encomenda, uma rota de serviço, composta por C cidades e C−1 estradas: a primeira cidade da rota de serviço é a origem da encomenda, a última o destino da encomenda. A rota de serviço não passa duas vezes pela mesma cidade, e o veículo escolhido para fazer o transporte de uma encomenda pode trafegar apenas pela rota de serviço definida.

Certo dia, no entanto, o veículo que executava uma entrega quebrou e precisou ser levado para conserto em uma cidade que não está entre as cidades de sua rota de serviço. A direção da Transportadora Dias quer saber qual é o menor custo total, em termos de pedágio, para que o veículo entregue a encomenda na cidade destino, a partir da cidade em que foi consertado, mas com uma restrição adicional: se em algum momento o veículo passar por uma das cidades que compõem a sua rota de serviço, ele deve voltar a obedecer a rota de serviço.

Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém quatro inteiros N, M, C e K (4 ≤ N ≤ 250, 3 ≤ M ≤ N×(N−1)/2, 2 ≤ C ≤ N−1 e C ≤ K ≤ N−1), representando, respectivamente, o número de cidades do país, o número de estradas, o número de cidades na rota de serviço e a cidade em que o veículo foi consertado. As cidades são identificadas por inteiros de 0 a N−1. A rota de serviço é 0, 1, ... , C−1, ou seja, a origem é 0, de 0 passa para 1, de 1 para 2 e assim por diante, até o destino C−1.

As M linhas seguintes descrevem o sistema rodoviário do país. Cada uma dessas linhas descreve uma estrada e contém três inteiros U, V e P (0 ≤ U, V ≤ N−1, U ≠ V, 0 ≤ P ≤ 250), indicando que há uma estrada interligando as cidades U e V com custo de pedágio P. O último caso de teste é seguido por uma linha contendo quatro zeros separados por espaço em branco.

Saída
Para cada caso de teste, o seu programa deve imprimir uma única linha, contendo um único inteiro T, o custo total mínimo necessário, em termos de pedágio, para que o veículo chegue ao destino.

Exemplo de Entrada	Exemplo de Saída
4 6 3 3             10
0 1 10              6
1 2 10              6
0 2 1
3 0 1
3 1 10
3 2 10
6 7 2 5
5 2 1
2 1 10
1 0 1
3 0 2
3 4 2
3 5 3
5 4 2
5 5 2 4
0 1 1
1 2 2
2 3 3
3 4 4
4 0 5
0 0 0 0

