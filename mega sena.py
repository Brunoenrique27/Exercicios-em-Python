from random import randint
lista = []
cont = 1
p = []
i = []
while True:
    try:
        escolha = int(input('Quantos jogos voce quer jogar?'))
    except (ValueError, TypeError):
        print('Opção invalida')
    else:
        print('Numeros gerados abaixo')
        break
cont = 1
while cont <= escolha:
    v = 1
    while v <= 6:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            v += 1
            lista.sort()
    for num in lista:
        print(f'{num} ', end='')
    print('',end='- ')
    for c in lista:
        if c % 2 == 0:
            p.append(c)
        else:
            i.append(c)
    print(f'numeros pares {len(p)} impares {len(i)}')
    p.clear()
    i.clear()
    lista.clear()
    cont += 1

