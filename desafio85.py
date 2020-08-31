## Crie um programa onde o usuário possa digitar sete valores numéricos
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
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


