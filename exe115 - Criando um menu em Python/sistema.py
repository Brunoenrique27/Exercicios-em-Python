from exe115.bibli.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar novas pessoas','Sair'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('CADASTRAR NOVO USUARIO')
        nome = str(input('Nome:'))
        idade = leiaInt('Idade:')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho('\033[31m\tSaindo do Sistema... Até logo\033[m')
        break
    else:
        print('\033[31mDigite apenas uma das 3 opçoes do Menu Principal\033[m')
    sleep(2)