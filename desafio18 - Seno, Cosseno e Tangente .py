print('Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente')

import math
ang = float(input('Digite um angulo qualquer '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'O angulo de {ang} tem o seno de {sen:.2f}\nO angulo de {ang} tem o cosseno de {cos:.2f}\nO angulo de {ang} tem a tangente de {tan:.2f}')