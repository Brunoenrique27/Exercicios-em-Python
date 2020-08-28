print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa')

import math
catopo= float(input('Qual o valor do comprimento do cateto oposto? '))
catadj = float(input('Qual o valor do cateto adjacente ? '))
hip = math.hypot(catopo,catadj)
print(f'O valor da hipotenusa é de {hip:.2f}')