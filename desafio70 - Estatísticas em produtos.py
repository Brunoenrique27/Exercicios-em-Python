print('*'*30)
print(' '*7,'LOJAO DO BATORE')
print('*'*30)
cont = total = totmil = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto? '))
    preço = float(input('Qual o valor R$'))
    cont += 1
    print('*'*30)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    total += preço
    print('*'*30)
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    if preço > 1000:
        totmil += 1
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1.000')
print(f'O nome do produto mais barato é {barato} que custa {menor}')