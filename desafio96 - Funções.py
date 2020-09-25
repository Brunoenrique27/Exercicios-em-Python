##Faça um programa que tenha uma função chamada área()
#Receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
print('Controle de Terrenos')
print('--------------------')
def area(larg, compri):
    s = larg * compri
    print(f'A area de um terreno de {larg}x{compri} é de {s}m²')

larg = float(input('LARGURA (m):'))
compri = float(input('COMPRIMENTO (m):'))
area(larg, compri)