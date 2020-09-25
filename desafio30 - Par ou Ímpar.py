print('Programa mostrara na tela se o numero é "PAR" ou "IMPAR"')

numero = int(input('Digite um numero:'))
if numero % 2 == 0: #resto da divisão do numero dividido por 2 for zero o numero é PAR
    print(f'O numero {numero} é "PAR"')
else:
    print(f'O numero {numero} é "IMPAR"')