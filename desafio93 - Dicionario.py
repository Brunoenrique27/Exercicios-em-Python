# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
gols = []
totgol = 0
jogador['nome'] = str(input('Nome do jogador:'))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,partidas):
    num = int(input(f'Quantos gols na partida {c}?'))
    totgol += num
    gols.append(num)
    jogador['gols'] = gols
    jogador['total'] = totgol
print('-='*30)
print(jogador)
print('-='*30)
for p, v in jogador.items():
    print(f'O campo {p} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(gols):
    print(f'   =>Na partida {k}, fez {v} gols.')
print(f'Foi um total de {totgol} gols.')