""" Entrada de dados monetários"""
from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

preço = dado.leiadinheiro('Digite o preço: R$ ')
moeda.resumo(preço, 80, 35)
