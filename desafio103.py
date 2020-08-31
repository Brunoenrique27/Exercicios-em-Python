##Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(n, g):
    if len(n) == 0:
        n = '<desconhecido>'
    if not gols.isnumeric():
        g = 0
        print(f'O jogador {n} fez {g} gols.')
    if gols.isnumeric():
        g = int(gols)
        print(f'O jogador {n} fez {g} gols.')



nome = str(input('Nome do jogador:'))
gols = str(input('Numero de gols:'))
ficha(nome, gols)