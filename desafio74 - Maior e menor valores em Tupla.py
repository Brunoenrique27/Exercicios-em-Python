##Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)
print('Os numeros são: ',end='')
for n in numeros:
    print(n, end=' ')
print(f'\nO maior numero é {max(numeros)}.')
print(f'E o menor numero é {min(numeros)}.')