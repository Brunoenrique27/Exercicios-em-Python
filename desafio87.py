matriz = [[],[],[]]
par = soma = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]')))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print(f'A soma dos valores pares é {par}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
for c in matriz[2]:
    soma += c
print(f'A soma dos valores da terceira coluna é {soma}')
