'''n = int(input('Digite um valor para saber seu fatorial:'))
tot = 1
for c in range(n, 1, -1): # o laço vai do numero escolhido ate 1
    tot *= c       # no primeiro laço o C multiplca por 1 e depois sucessivamente
    print(tot)
print(f'o fatorial é {tot}')'''

n = int(input('Cálculo de fatorial (Usando while)\nDigite um número inteiro: '))
total = n
c = n
print(f'{n}! = {n} ', end='')
while c != 1:
    c -= 1
    print(f'x {c} ', end='')
    total = total * c
print(f'= {total}')
print('FIM')