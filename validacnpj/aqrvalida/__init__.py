REGRESSIVO = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def formata(cnpj):
    for item in '-/.':  # retira todos os pontos e hifen barra do cnpj
        cnpj = cnpj.replace(item, '')
    return cnpj


def verificador(cnpj):
    sequencia = str(cnpj[0]) * len(cnpj)  ##Evita sequencias. Ex.: 11111111111, 00000000000...
    if cnpj == sequencia:
        return print('CNPJ Invalido, não é permitido sequencias')
    else:
        primeiro = cnpj[:-2]  # eliminina os dois ultimos numeros do CNPJ
        segundo = cnpj[:-1]
        digito1 = valida(primeiro, 1)  # aqui sera efetuado pra saber o primeiro numero do CNPJ
        digito2 = valida(segundo, 2)    ##aqui sera efetuado pra saber o segundo numero do CNPJ
        resultado = confere(cnpj, digito1, digito2)
        return resultado


def valida(cnpj, digito):  # aqui recebo a sequencia do cnpj feito o fatiamento e o digito
    if digito == 1:
        regressivo = REGRESSIVO[1:]  # aqui o regressivo iniciara do 5
    elif digito == 2:
        regressivo = REGRESSIVO
    tot = 0
    for indice, valor in enumerate(regressivo):
        tot += int(cnpj[indice]) * valor  # obtemos o total dos numeros
    resto = 11 - (tot % 11)
    if resto > 9:
        digito = 0
    else:
        digito = resto
    return digito


def confere(cnpj, digito1, digito2):
    if int(cnpj[12]) == digito1 and int(cnpj[13]) == digito2:
        print('CNPJ VALIDO!')
    else:
        print('Esse CNPJ é Invalido.')
