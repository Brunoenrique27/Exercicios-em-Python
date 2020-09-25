print('Leia um numero inteiro e diga se ele é ou nao um numero primo')#primo é um numero dividido por 1 e ele mesmo
n = int(input('Digite um numero:'))
tot = 0
for c in range(1,n+1):
    if n % c == 0:
        tot += 1
if tot == 2:
    print(f'O numero {n} é primo')
else:
    print(f'O numero {n} foi dividido {tot} vezes')
    print(f'O numero {n} nao é primo')
