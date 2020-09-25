print('Leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto')
sexo = str(input('Digite seu sexo [M/F]:')).upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos.\nDigite seu sexo [M/F]:')).strip().upper()[0]
print(f'Opção valida seu sexo é {sexo}.')