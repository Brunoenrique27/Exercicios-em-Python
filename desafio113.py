def leiaint(n):
    while True:
        try:
            tipo = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro valido.\033[m')
        else:
            return tipo


def leiafloat(real):
    while True:
        try:
            n = float(input(real))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero Real valido.\033[m')
        else:
            return n


n = leiaint('Digite um numero intero:')
real = leiafloat('Digite um numero Real:')
print(f'O valor inteiro digitado foi {n} e o real foi {real}')