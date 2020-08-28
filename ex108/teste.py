from ex108 import moeda
preço = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.formatmoeda(preço)} é {moeda.formatmoeda(moeda.metade(preço))}.')
print(f'O dobro de {moeda.formatmoeda(preço)} é {moeda.formatmoeda(moeda.dobro(preço))}.')
print(f'Aumentando em 10%, temos {moeda.formatmoeda(moeda.aumentar(preço, 10))}.')
print(f'Reduzindo em 13%, temos {moeda.formatmoeda(moeda.diminuir(preço, 13))}.')
