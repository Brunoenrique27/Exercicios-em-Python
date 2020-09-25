print('Crie um programa que mostre todos os numeros pares que estao no intervalo entre 1 e 50')

for c in range(2, 51, 2):
    print(c, end=' ')
print('Fim')

from random import randint
for c in range(2, 51, 2):
    o = randint(31, 37)
    print(f'\033[{o}m{c}\033[m', end=' ')

