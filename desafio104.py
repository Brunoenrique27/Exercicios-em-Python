def leiaInt(n):
    while True:
        valor = str(input(f'{n}'))
        if valor.isnumeric():
            valor = int(valor) # se for digitado um valor inteiro, passo a variavel pra int
            return valor
        else:
            print('\033[31mDigite novamente um numero\033[m')

n = leiaInt('Digite um numero:')
print(f'Voce acabou de digitar o numero {n}.')