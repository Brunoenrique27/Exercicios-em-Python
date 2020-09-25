print('Calcule a soma de entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 a 500.')
soma = 0
cont = 0
for n in range(1, 501,2):
    if n % 3 == 0:
        cont += 1         #aqui o programa faz a contagem do total dos multiplos de 3
        soma += n         #aqui ele realiza a soma de todos os numeros
        print(n, end=' ')
print(f'\nA Soma de {cont} valores solicitados é {soma}')

s = 0
cont = 0
for n in range(3, 500,3):
    if n % 2 != 0:
        cont += 1
        s = s + n
        print(n, end= " ")
print(f'\nA Soma de {cont} valores solicitados é {s}')


