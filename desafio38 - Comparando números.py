entrada = "COMPARAÇOES DE VALORES"
print(f'\033[34m' "*"*50,"\033[m")
print(f'{entrada:^50}')
print(f'\033[34m' "*"*50,"\033[m")

n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))

if n1 > n2:
    print(f'O PRIMEIRO valor é o maior!')
elif n2 > n1:
    print(f'O SEGUNDO valor é maior')
else:
    print('Nao existe valor maior, os dois sao IGUAIS.')
