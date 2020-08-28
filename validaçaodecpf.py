while True:
    cpf = input('Digite seu cpf:')
    if len(cpf) > 11 or len(cpf) < 11:
        print('Digite apenas 11 numeros do seu CPF')
    if len(cpf) == 11:
        novocpf = cpf[:-2]    ## 9 digitos do cpf
        novocpf2 = cpf[:-1]   ## 10 digitos do cpf
        soma1 = soma2 = tot1 = tot2 = digito1 = digito2 = 0
        lista1 = [10,9,8,7,6,5,4,3,2,1]
        lista2 = [11,10,9,8,7,6,5,4,3,2,1]

        #para descobrir o primeiro digito soma os 9 numeros do cpf
        for indice in range(9):
            soma1 += int(novocpf[indice]) * lista1[indice]
        tot1 = soma1 % 11
        if tot1 < 2:    # se o resto for menor que 2, recebe o digito 0
            digito1 = 0
        else:
            digito1 = 11 - tot1

        #para descobrir o segundo digito soma os 10 digitos do cpf
        for indice in range(10):
            soma2 += int(novocpf2[indice]) * lista2[indice]
        tot2 = soma2 % 11

        if tot2 < 2:  # se o resto for menor que 2, recebe o digito 0
            digito2 = 0
        else:
            digito2 = 11 - tot2

        sequencia = str(cpf[0]) * len(cpf)  # Evita sequencias. Ex.: 11111111111, 00000000000...
        if cpf == sequencia:
            print('\033[31mCPF invalido\033[m')
        elif digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
            print(f'CPF valido')
            break
        else:
            print('\033[31mCPF invalido\033[m')
