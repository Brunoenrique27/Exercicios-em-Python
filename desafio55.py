print('leia o peso de cinco pessoas, mostre qual foi o maior e o menor peso lido:')
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite {c}º peso:'))
    if c == 1: #aqui mostrara o numero do primeiro laço
        maior = peso 
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso é {maior}kgs')
print(f'o menor peso é {menor}kgs')