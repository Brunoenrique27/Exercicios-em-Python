from random import randint
cont = 0
print('=-='*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-='*10)
while True:
    jogador = int(input('Digite um numero:'))
    opçao = ' '
    while opçao not in 'PI':
        opçao = str(input('Par ou Impar?[P/I]:')).strip().upper()[0]
    maquina = randint(1,10)
    soma = maquina + jogador
    if soma % 2 == 0 and opçao == 'P':
        print('*'*30)
        print(f'Voce jogou {jogador} a maquina jogou {maquina} a soma deu {soma} é PAR voce ganhou')
        print('*'*30)
        cont += 1
    else:
        if soma % 2 != 0 and opçao == 'P':
            break
    if soma % 2 != 0 and opçao == 'I':
        print('*'*30)
        print(f'Voce jogou {jogador} a maquina jogou {maquina} a soma deu {soma} é IMPAR voce ganhou ')
        print('*'*30)
        cont += 1
    else:
        if soma % 2 == 0 and opçao == 'I':
            break
    print('Vamos jogar novamente...')
print('Voce PERDEU')
print(f'GAME OVER! voce venceu {cont} vezes.')