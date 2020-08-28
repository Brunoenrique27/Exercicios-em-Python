lista = []
pessoas = {}
tot = media = 0
while True:
    pessoas['nome'] = str(input('Nome:'))
    pessoas['sexo'] = str(input('Sexo[F/M] ')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade:'))
    tot += pessoas['idade']
    lista.append(pessoas.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*40)
print(f'Foram cadastradas {len(lista)} pessoas.')
media = tot / len(lista)
print(f'A média de idade do grupo é {media:.1f}')
print(f'As mulheres cadastradas foram:', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=' ')
print(f'\nLista das pessoas que estão acima da média:')
for c in lista:
    if c['idade'] >= media:
        print(f'nome = {c["nome"]} sexo = {c["sexo"]} idade = {c["idade"]}')