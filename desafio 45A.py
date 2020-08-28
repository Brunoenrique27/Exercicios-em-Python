print("*"*50)
print(f'{"JOKENPO":^50}')
print("*"*50)
print('''Escolha uma das opçoes abaixo
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
import random
import time
jogador = ''
while jogador != 0 and jogador != 1 and jogador != 2:
    jogador = int(input('Qual sua jogada:'))
    if jogador != 0 and jogador != 1 and jogador !=2:
        print('OPÇÃO INVALIDA ESCOLHA UMA DAS EXIBIDAS NA TELA')
lista = ["Pedra", "Papel", "Tesoura"]
maquina = random.randint(0,2)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
print('-='*25)
print(f'VOCE jogou {lista[jogador]}')
print(f'MAQUINA jogou {lista[maquina]}')
print('-='*25)

if maquina == 0 and jogador == 1:
    print('VOCE GANHOU DA MAQUINA')
elif maquina == 1 and jogador == 0:
    print('VOCE PERDEU DA MAQUINA')
elif maquina == 2 and jogador == 1:
    print('VOCE PERDEU DA MAQUINA')
elif maquina == 2 and jogador == 0:
    print('VOCE GANHOU DA MAQUINA')
elif maquina == 1 and jogador == 2:
    print('VOCE GANHOU DA MAQUINA')
elif maquina == 2 and jogador == 0:
    print('VOCE GANHOU DA MAQUINA')
else:
    print('EMPATE')
