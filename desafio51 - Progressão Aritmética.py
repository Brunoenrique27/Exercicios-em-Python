print('Leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressão')

num = int(input('\nDigite o Primeiro número da PA: '))
razao = int(input('Digite a Razão da PA: '))
for c in range(1, 11):
    print(num, end=' ')
    num += razao
print('Acabou')