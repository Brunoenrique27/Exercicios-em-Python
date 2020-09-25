print('Faça um programa que leia um ano qualquer e mostre se ele é bissexto\n')
#print("""É divisível por 4 e não é por 100? Bissexto
#É divisível por 4, por 100 e por 400?  Bissexto
#É divisível por 4, por 100 e não é por 400? Não é bissexto
#Não é divisível por 4? Não é bissexto\n""")
from datetime import date
ano = int(input('Que ano voce quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO!')
else:
    print(f'O ano de {ano} NÃO É BISSEXTO!')