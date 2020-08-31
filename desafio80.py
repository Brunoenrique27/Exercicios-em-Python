## Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = []
for cont in range(0,5):
    num = int(input(f'Digite um valor:'))
    if cont == 0:
        lista.append(num)
    else:
        if num >= max(lista):
            lista.insert(lista[-1], num)
        elif num < min(lista):
            lista.insert(0, num)
        elif num < lista[1]:
            lista.insert(1,num)
        elif num < lista[2]:
            lista.insert(2, num)
        elif num < lista[3]:
            lista.insert(3,num)
print(lista)