#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
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