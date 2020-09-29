""" Transformando módulos em pacotes"""

from ex111.utilidadesCeV import moeda
preço = float(input('Digite o preço: R$ '))
moeda.resumo(preço, 80, 5)