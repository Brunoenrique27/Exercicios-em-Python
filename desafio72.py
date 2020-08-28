cont = 'zero', 'um', 'dois', 'três', 'quatro',\
          'cinco', 'seis', 'sete', 'oito', 'nove',\
          'dez', 'onze', 'doze', 'treze', 'catorze',\
          'quinze', 'dezesseis', 'dezessete', 'dezoito',\
          'dezenove', 'vinte'
while True:
    numero = int(input('Digite um numero entre 0 e 20:'))
    if numero > 20 or numero < 0:
        print('Digite novamente.', end=' ')
    if 0 <= numero <= 20:
        print(f'Você digitou o numero {(cont[numero])}.')
        escolha = ' '
        while escolha not in 'SN':
            escolha = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
        if escolha == 'N':
            break
print('FIM... PROGRAMA ENCERRADO.')