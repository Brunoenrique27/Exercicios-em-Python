print('Crie um programa que leia seu numero real e mostre sua parte inteira')

from math import trunc
num = float(input('Digite um numero '))
numint = trunc(num)
print(f'O numero {num} tem a parte inteira {numint}')
