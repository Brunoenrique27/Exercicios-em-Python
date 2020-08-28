print('Leia 6 numeros inteiros e mostre a soma apenas daqueles que forem PARES. Se o valor digitado foi IMPAR, desconsidere-o')
soma = 0
cont = 0
cont1 = 0
for c in range(1, 7):
    n = int(input(f'Digite {c}º valor:'))
    if n % 2 == 0:
        soma += n
        cont += 1
    else:
        cont1 += +1
print(f'Voce informou {cont} numeros pares a soma entre eles é {soma}')
print(f'Voce informou {cont1} numero impares')

