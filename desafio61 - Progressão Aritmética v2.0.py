##lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
ptermo = int(input('Digite o primeiro termo de uma PA:'))
razao = int(input('Digite a razão:'))
laço = 0
while laço < 10:
    print(f'{ptermo} >>', end=' ')
    ptermo += razao
    laço += 1