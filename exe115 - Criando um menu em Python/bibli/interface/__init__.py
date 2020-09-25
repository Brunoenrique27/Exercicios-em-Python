def linha():
    print('-'*42)

def cabecalho(msg):
    linha()
    print(f'{msg}'.center(42))
    linha()

def menu(lista):
    cabecalho('\033[30mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    linha()
    escolha = leiaInt('\033[33mSua Opção:\033[m')
    return escolha


def leiaInt(msg):
    try:
        opc = int(input(msg))
    except (ValueError, TypeError):
        print('Digite um numero valido')
    else:
        return opc