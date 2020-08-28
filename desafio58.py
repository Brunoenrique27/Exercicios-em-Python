print('Acerte numero de 0 a 10, no final ira mostrar quantas tentativas teve ate vc acertar o numero da maquina')
from random import randint
maquina = randint(0, 10) #aqui a maquina sorteia um numero
palpite = 0
jogador = '' #aqui variavel sem valor
while jogador != maquina:          # enquanto o jogador for diferente do numero escolhido pela maquina
    jogador = int(input('Escolha um numero:'))
    palpite += 1           #faz a soma de quantas vezes vc escolheu um numero
    if jogador < maquina:
        print('Mais ... tente mais uma vez')
    elif jogador > maquina:
        print('Menos... tente mais uma vez')
if maquina == jogador:
    print(f'voce acertou e precisou de {palpite} tentativas. Parabens!')