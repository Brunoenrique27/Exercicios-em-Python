from time import sleep
opção = 0
valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
while opção != 5: #enquanto a opção nao for 5 o programa continuara rodando
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MOSTRE O MAIOR NUMERO
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('>>>>>>>>>Escolha uma opção:'))
    if opção > 5: #se digitar um numero maior que 5 o programa vai pedir pra escolher uma opção valida
        opção = int(input('Digite novamente opção INVALIDA.\nEscolha uma opção:'))
    elif opção == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} o total é {soma} ')
        print('===================================================')
    elif opção == 2:
        mult = valor1 * valor2
        print(f'O resultado entre {valor1} x {valor2} é {mult}')
        print('===================================================')
    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
            print(f'O maior valor é {maior}')
        else:
            maior = valor2
            print(f'O maior valor é {maior}')
    elif opção == 4:
        print('INFORME OS NUMEROS NOVAMENTE')
        valor1 = int(input('Digite o primeiro valor:'))
        valor2 = int(input('Digite o segundo valor:'))
    elif opção == 5:
        print('SAINDO DO PROGRAMA...')
        sleep(2)
        print('FIM')
