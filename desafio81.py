lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('Quer continuar?[S/N]:')).strip().upper()[0]
    if opçao == 'N':
        break
print('-='*30)
print(f'Foi digitado total de {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
    print(f'o numero 5 aparece na posiçao {lista.index(5)}.')
else:
    print('O valor 5 nao faz parte da lista.')
