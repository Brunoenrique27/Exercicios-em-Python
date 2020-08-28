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