def leiadinheiro(msg, taxa=0, taaxa=0):
    while True:
        opçao = str(input(msg)).strip().replace(',', '.')
        if opçao.isnumeric():
            opçao = int(opçao)
            return opçao
        elif opçao.isalpha() or opçao.isalnum():
            print(f'\033[31m{opçao} é um valor invalido. Digite novamente\033[m')
        elif opçao == '':
            print('\033[31mNao existe valor a ser Executado, opçao invalida. Digite novamente.\033[m')
        else:
            return float(opçao)


def leiaInt(n):
    while True:
        valor = str(input(f'{n}'))
        if valor.isnumeric():
            valor = int(valor) # se for digitado um valor inteiro, passo a variavel pra int
            return f'Voce acabou de digitar o numero {valor}.'
        else:
            print('\033[31mDigite novamente um numero\033[m')


