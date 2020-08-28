tabela = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio',\
        'Atlhetico-PR', 'São Paulo', 'Internacional', 'Corinthians',\
        'Fortaleza', 'Goias', 'Bahia', 'Vasco', 'Atlético-MG',\
        'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',\
        'Chapecoense', 'Avai'
for time in tabela:
        print(time)
print('*'*15)
print(f'Os 5 primeiros colocados são {tabela[0:5]}')
print('*'*15)
print(f'Os ultimos 4 colocados da tabela são {tabela[-4:]}')
print('*'*15)
print(f'A lista dos times em ordem alfabetica é {sorted(tabela)}')
print('*'*15)
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}º posição do campeonato.')
print('*'*15)
print(f'O Campeonato é formado por {len(tabela)} times.')