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
