turma = []
dado = []
peso = []
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    turma.append(dado.copy())
    peso.append(dado[1])
    dado.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Foram cadastradas {len(turma)} pessoas')
print(f'O maior peso foi {max(peso)}. Peso de', end=' ')
for c in turma:
    if c[1] == max(peso):
        print(f'{c[0]}', end=' ')
print(f'\nO menor peso foi {min(peso)}. Peso de', end=' ')
for c in turma:
    if c[1] == min(peso):
        print(f'{c[0]}', end=' ')
