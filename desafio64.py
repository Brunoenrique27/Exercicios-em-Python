c = 0
numero = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um numero ou [999 para parar]:'))
    soma += numero
    c += 1
print(f'Voce digitou {c-1} numeros\nA soma entre eles foi de {soma-999}')