lista = []
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1+nota2) /2
    lista.append([nome,[nota1,nota2],media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*40)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-------------------------------')
for p, a in enumerate(lista):
    print(f'{p:<4} {a[0]:<10}{a[2]:>8.1f}')
print('----------------------------')
while True:
    print('*'*35)
    op = int(input('Mostrar a nota de qual aluno? (999 para interromper)'))
    for p, a in enumerate(lista):
        if op == p:
            print(f'A nota de {a[0]} são {a[1]}')
    if op == 999:
        break
print('PROGRAMA FINALIZADO...')