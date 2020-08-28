valor = int(input('Valor do saque: R$ '))
ced50 = resto = ced20 = 0
while True:
    ced50 = valor // 50
    resto = valor - (ced50*50)
    ced20 = resto // 20
    resto = resto - (ced20*20)
    ced10 = resto // 10
    resto = resto - (ced10*10)
    ced1 = resto // 1
    resto = resto - resto
    if resto == 0:
        break
if ced50 > 0:
    print(f'{ced50} cedulas de 50 reais.')
if ced20 > 0:
    print(f'{ced20} cedulas de 20 reais.')
if ced10 > 0:
    print(f'{ced10} cedulas de 10 reais.')
if ced1 > 0:
    print(f'{ced1} cedulas de 1 real.')