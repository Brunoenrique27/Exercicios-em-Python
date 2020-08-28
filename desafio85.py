pares = []
impar = []
lista = [pares,impar]
for p in range(1,8):
    num = int(input(f'Digite o {p}º valor:'))
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impar.append(num)
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores impares digitados foram: {sorted(impar)}')


