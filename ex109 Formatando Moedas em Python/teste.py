from ex109 import moeda
preço = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.formatado(preço)} é {moeda.metade(preço, True)}.')
print(f'O dobro de {moeda.formatado(preço)} é {moeda.dobro(preço, True)}.')
print(f'Aumentando em 10%, temos {moeda.aumentar(preço, 10, True)}.')
print(f'Reduzindo em 13%, temos {moeda.diminuir(preço, 13, True)}.')
