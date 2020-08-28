from random import randint
from time import sleep
from operator import itemgetter
lista = []
jogo = {}
print('Valores SORTEADOS')
jogo['jogador1'] = randint(1,6)
jogo['jogador2'] = randint(1,6)
jogo['jogador3'] = randint(1,6)
jogo['jogador4'] = randint(1,6)
lista.append(jogo.copy())
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('  == RANKING DOS JOGADORES ==  ')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} tirou {v[1]}')
    sleep(1)