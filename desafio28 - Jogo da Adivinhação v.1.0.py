## Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print("-=-"*20)
print('Qual numero voce acha que foi escolhido pela maquina? ')
print("-=-"*20)
n = randint(0, 5) #aqui a o computador fara o sorteio
sorteio = int(input('Digite o numero que vc acha: ')) #aqui o jogador escolhera o numero
print('PROCESSANDO...')
sleep(2)
print(f'O numero sorteado pela maquina foi {n}')
print("+-+"*20)
if n == sorteio:
    print(f'Voce escolheu o numero {sorteio} e acertou PARABENS')
else:
    print(f'Infelizmente voce PERDEU o numero escolhido pela maquina foi {n} ')
print("+-+"*20)