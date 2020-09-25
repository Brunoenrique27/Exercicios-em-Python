##Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla
# No final, mostre: Quantas vezes apareceu o valor 9. Em que posição foi digitado o primeiro valor 3. Quais foram os números pares.
lista = int(input('Digite um numero:')), \
        int(input('Digite um numero:')), \
        int(input('Digite um numero:')),\
        int(input('Digite um numero:'))
print(f'Voce digitou os numeros {lista}')
print(f'O numero 9 apareceu {lista.count(9)} vezes.')    # AQUI VEJO A POSIÇÃO QUE ESTA O 9 NA TUPLA
if 3 in lista:                                          #SE EXISTE 3 NA TUPLA
    print(f'O valor 3 apareceu na posição {lista.index(3,0)+1} ')        #AQUI VEJO QUAL POSIÇAO O 3 FOI DIGITADO NA TUPLA
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram', end='')
for numero in lista:             #declarei como 'numero' para saber cada numero dentro da lista
    if numero % 2 == 0:
        print(f' {numero}', end='')
    numero +=1