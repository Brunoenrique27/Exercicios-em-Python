## Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
lista = []
jogador = {}
gols = []
while True:
    print('--'*25)
    jogador['nome'] = str(input('Nome do Jogador:'))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gol'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    lista.append(jogador.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*25)
print('cod',end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
for pos, v in enumerate(lista):
    print(f'{pos:>3}',end=' ')
    for c in v.values():
        print(f'{str(c):<15}',end=' ')
    print()
print('--'*25)
while True:
    opção = int(input('Mostrar dados de qual jogador? (999 parar sair):'))
    if opção == 999:
        break
    if opção >= len(lista):
        print(f'Não existe jogador {opção}')
    else:
        for k, v in enumerate(lista):
            if opção == k:
                print(f'-- LEVANTAMENTO DO JOGADOR: {v["nome"]}')
                for k, v in enumerate(lista[opção]['gol']):
                    print(f'\tNo jogo {k+1} fez {v} gols.')
print('PROGRAMA FINALIZADO')