## Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
jogos = []
print('*'*30)
print('     SORTEIO MEGA SENA         ')
print('*'*30)
quantidade = int(input('Quantos sorteios voce deseja?'))
for c in range(0,quantidade):
    c = 1
    while c <= 6:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            c += 1
    lista.sort()
    jogos.append(lista.copy())
    lista.clear()
for v, c in enumerate(jogos):
    print(f'O jogo {v+1}: {c}')
    sleep(1)
print('*'*30)
print('-='*5,'BOA SORTE','-='*5)