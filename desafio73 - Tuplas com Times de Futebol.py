##Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação
# Depois mostre: Os 5 primeiros times. Os últimos 4 colocados. Times em ordem alfabética.  Em que posição está o time da Chapecoense.
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