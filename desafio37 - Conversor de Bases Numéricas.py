num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversoes: 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção:'))

if opcao == 1:
    print(f'{num} convertido para BINARIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para EXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção invalida. Tente novamente.')