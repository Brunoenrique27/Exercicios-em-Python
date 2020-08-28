def fatorial(n,show=0):
    """Calcula o fatorial
    :param n: o numero a ser calculado
    :param esc: usuario escolhe o tipo de exibição na tela
    :return : retorna o valor fatorial do numero n"""
    f = 1
    if show == 0:
        for c in range(n, 0, -1):
            f *= c
        return f
    else:
        for c in range(n, 0, -1):
            print(c,end=' ')
            if c > 1:
                print('x ',end='')
            f *= c
        return f'= {f}'

num = int(input('Escolha um numero pra calcular o fatorial:'))
esc = int(input('Deseja exibir na tela somente o resultado digite 0 ou 1 para exibir o calculo em passo a passo:'))
print(fatorial(num, esc))