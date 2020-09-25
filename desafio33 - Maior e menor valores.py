print('Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor')

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'o numero maior é {n1}')
if n2 > n1 and n2 > n3:
    print(f'O numero maior sera {n2}')
if n3 > n1 and n3 > n2:
    print(f'O numero maior sera {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor numero sera {n1}')
if n2 < n1 and n2 < n3:
    print(f'O menor numero sera {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor numero sera {n3}')