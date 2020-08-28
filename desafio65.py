usuario = ''
soma = cont = media = maior = menor = 0
while usuario != 'N':
    numero = int(input('Digite um numero:'))
    usuario = str(input('Quer continuar [S/N]:')).strip().upper()[0] #aqui no [0] ele considera a primeira letra se o usuario escrever nome inteiro
    soma += numero
    cont += 1
    media = soma / cont
    if cont == 1:             #primeiro laço eu defino o 1º numero como maior e menor
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print(f'Voce digitou {cont} numeros \nA soma de todos os numeros foi {soma} a media foi {media}\nO maior numero é {maior} e o menor numero foi {menor}')
