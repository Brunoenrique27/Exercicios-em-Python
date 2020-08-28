print('Crie um programa que leia o nome de uma cidade e diga se ele começa ou nao com a palavra "Santo"')
nome = (input('Qual nome da cidade? ')).upper().strip()
print('Ela começa com a palavra Santo?')
print(nome[:5] == 'SANTO')