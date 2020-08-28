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