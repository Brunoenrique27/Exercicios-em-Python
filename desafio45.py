a = "*"*40
b = 'JOKENPO'
print(f'\033[34m{a}')
print(f'\033[1;31m{b:=^40}\033[m')
print('\033[34m'"*"*40)
print('\033[31mREGRAS\033[m:Pedra ganha da Tesoura (a amassa e quebra)\nTesoura ganha do Papel(o corta)\nPapel ganha da Pedra(a embrulha)\nNo caso que os participantes coincidam mostrando o mesmo símbolo, acontece um empate e se joga outra vez até desempatar')
import random
import time
print('\033[36mOPÇOES DE JOGADA\033[m')
print('[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')
jogador = int(input('Qual é sua jogada:'))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('JOGADA INVALIDA OPÇAO INEXISTENTE')
    quit()
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
lista = ['Pedra','Papel','Tesoura']
maquina = random.randint(0,2)
print("=-="*9)
print(f'Voce escolheu {lista[jogador]}')
print(f'Maquina escolheu {lista[maquina]}')
print("=-="*9)

if maquina == 0:            #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:               #papel
        print('VOCE GANHOU')
    elif jogador == 2:           #tesoura
        print('VOCE PERDEU PRA MAQUINA')
    else:
        print('JOGADA INVALIDA')
elif maquina == 1:       #papel
    if jogador == 0:      #pedra
        print('VOCE PERDEU PRA MAQUINA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:          #tesoura
        print('VOCE GANHOU')
    else:
        print('JOGADA INVALIDA')
elif maquina == 2:
    if jogador == 0:     #pedra
        print('VOCE GANHOU')
    elif jogador == 1: #papel
        print('VOCE PERDEU PRA MAQUINA')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
