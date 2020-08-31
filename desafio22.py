# Crie um programa que leia o nome completo de uma pessoa e mostre:
# nome com letras maiusculas e minusculas, quantidade de letras sem contar espaço

nome = str(input('Digite um nome inteiro ')).strip()
print(f'Seu nome com todas as letras maiscula é {nome.upper()}')
print(f'Seu nome com todas as letras minuscula é {nome.lower()}')
print(f'A quantidade de letras do seu nome é {len(nome)-nome.count(" ")}')
lista = nome.split()
print(f'Seu primeiro nome é {lista[0]} e tem {len(lista[0])} letras')
