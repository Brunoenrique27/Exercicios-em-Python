while True:
    cpf = input('Digite seu cpf:')
    if len(cpf) < 11 or len(cpf) > 11:
        print('Numero invalido digite seu CPF corretamente com apenas numeros')
    elif len(cpf) == 11 and cpf.isnumeric():
       print(f'Seu cpf é {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
    resp = str(input('Quer conti'))
    if resp == 'n':
        break
