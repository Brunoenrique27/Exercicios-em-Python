#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre: Quantas pessoas foram cadastradas. Uma listagem com as pessoas mais pesadas. Uma listagem com as pessoas mais leves.
turma = []
dado = []
peso = []
while True:
    dado.append(str(input('Nome:')))
    dado.append(int(input('Peso:')))
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
        print(f'{c[0]}', end=' ')    # nome da pessoa
print(f'\nO menor peso foi {min(peso)}. Peso de', end=' ')
for c in turma:
    if c[1] == min(peso):
        print(f'{c[0]}', end=' ')   # nome da pessoa
