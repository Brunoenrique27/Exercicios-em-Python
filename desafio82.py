## Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um valor:')))
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('Quer continuar?[S/N]:')).strip().upper()[0]
    if opçao == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:    #se o numero dentro da lista for dividido por 2 e resto zero, ele é par e add dentro da lista par
        listapar.append(v)
    if v % 2 != 0:
        listaimpar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de numeros pares é {listapar}')
print(f'A lista de numeros impares é {listaimpar}')