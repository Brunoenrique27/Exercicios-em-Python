def formatado(preço):
    return f'R${preço:.2f}'.replace('.', ',')


def metade(preço, resp=False):
    v = preço / 2
    if resp == False:
        return v
    else:
        return formatado(v)


def dobro(preço, resp=False):
    v = preço * 2
    if resp == False:
        return v
    else:
        return formatado(v)


def aumentar(preço, taxa, resp=False):
    v = preço + (preço / 100 * taxa)
    if resp == False:
        return v
    else:
        return formatado(v)


def diminuir(preço, taxa, resp=False):
    v = preço - (preço / 100 * taxa)
    if resp == False:
        return v
    else:
        return formatado(v)


def resumo(preço=0, aum=0, red=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{formatado(preço)}')
    print(f'Dobro do preço:\t\t{dobro(preço, True)}')
    print(f'Metade do preço:\t{metade(preço, True)}')
    print(f'{aum}% de aumento:\t\t{aumentar(preço, aum, True)}')
    print(f'{red}% de redução:\t\t{diminuir(preço, red, True)}')