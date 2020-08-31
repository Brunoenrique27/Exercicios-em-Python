##Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
numeros = []
def sorteio():
    for c in range(1,6):
        numeros.append(randint(1,10))
    print(f'os valores sorteados foram:', end=' ')
    for c in numeros:
        print(f'{c}',end=' ')
        sleep(0.4)
    print('PRONTO!')


def soma():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos numeros pares da lista {numeros} foram {soma}.')

sorteio()           #aqui meu programa vai mostrar o resultado de defsorteio
soma()              #aqui mostrara o resultado da soma dos numeros pares