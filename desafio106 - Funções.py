##Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
def linha (msg):
    tam = len(msg) + 4
    print('\033[30;44m~' * tam)
    print(f'  {msg}')
    print('~' * tam)


def manual(valor):
    txt = f'Acessando os dados de `{valor}´'
    tam = len(txt) +6
    print('\033[30;42m~'*tam)
    print(f'  {txt}')
    print('~'*tam)
    print('\033[m\033[7;30m')
    help(valor)
    print('\033[m')


comando = ''
while True:
    linha('SISTEMA DE AJUDA PyHELP')
    comando = str(input('\033[mFunção ou Biblioteca ou digite a palavra fim pra sair? '))
    if comando.upper() == 'FIM':
        break
    else:
        manual(comando)
print('\033[30;41m~'* 12)
print('  ATÉ LOGO')
print('~'* 12)
print('\033[m')