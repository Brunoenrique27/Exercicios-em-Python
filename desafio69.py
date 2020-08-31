##A) quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados.
# quantas mulheres tem menos de 20 anos.

maior = toth = menor = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    print('*'*30)
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('Quer continuar [S/N]:')).strip().upper()[0]
    print('*'*30)
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        toth += 1
    elif sexo == 'F' and idade < 20:
        menor += 1
    if opçao == 'N':
        break
print(f'{maior} pessoas já sao maiores de 18 anos.')
print(f'Foram cadastrados {toth} homens.')
print(f'Existe {menor} mulheres com menos de 20 anos.')