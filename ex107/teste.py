"""Exercitando-módulos-em-Python"""

from ex107 import moeda
preço = float(input('Digite o preço: R$ '))
print(f'A metade de {preço} é {moeda.metade(preço)} ')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(preço, 10)}')
print(f'Reduzindo em 13%, temos {moeda.diminuir(preço, 13)}')
