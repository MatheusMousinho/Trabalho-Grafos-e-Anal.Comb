O problema da torre de Hanoi é super famoso, entretanto poucas pessoas sabem a lenda original: Diz-se que macacos foram responsabilizados a resolver o problema e que quando eles terminarem, o mundo acaba.

O problema consiste de 3 pinos, e que no primeiro pino existe uma pilha de discos, um maior do que o outro, empilhados. Como se sabe, não é permitido colocar um disco maior em cima do menor. Ou seja, para transferir certo disco, é necessário remover todos os menores anteriormente. Além disso, só é permitido mover um disco por vez.

O problema é resolvido quando todos os discos do primeiro pino são transferidos para o terceiro pino.

Sabe-se que os macacos começaram a trabalhar a meia noite (00:00), e que eles trabalham 24hs por dia sem parar e demoram, no mínimo, 1 segundo para movimentar cada disco. Sua tarefa é prever em qual horário do dia ou da noite, no formato hh:mm:ss, do tempo mínimo que eles podem terminar.

Entrada A entrada consiste em uma única linha contendo um número 0 < X < 1040, que é o número de discos que os macacos tem que movimentar.

Saída A saída consiste em um string no formato A:B:C, onde 0 <= A < 24 e 0 <= B, C < 60

Exemplo de Entrada Exemplo de Saída 1 00:00:01

2 00:00:03

3 00:00:07

4 00:00:15
