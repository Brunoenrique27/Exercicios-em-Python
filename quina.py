from random import randint
from time import sleep
lista = []
escolha = int(input('Quantos jogos voce quer jogar? '))
cont = 1
while cont <= escolha:       #quantidade de jogos
    v = 1
    while v <= 6:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            lista.sort()
            v +=1
    for c in lista:
        print(f'{c} ',end='')
        sleep(0.3)
    print()
    lista.clear()
    cont += 1