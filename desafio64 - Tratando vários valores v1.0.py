##Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
c = 0
numero = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um numero ou [999 para parar]:'))
    soma += numero
    c += 1
print(f'Voce digitou {c-1} numeros\nA soma entre eles foi de {soma-999}')