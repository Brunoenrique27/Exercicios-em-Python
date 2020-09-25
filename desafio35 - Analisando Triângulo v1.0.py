print('Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo')

print('Analisador de triangulo')
l1 = float(input('Digite um lado '))
l2 = float(input('Digite o segundo lado '))
l3 = float(input('Digite o terceiro lado '))

if  l1 + l2 > l3 and l2 + l1 > l3 and l3 + l1 > l2:
    print(f'Eles podem formar um triangulo ? SIM')
else:
    print(f'Eles podem formar um triangulo ? NAO')