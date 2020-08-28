from exe115.bibli.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com Sucesso')
        a.close()

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro na abertura do arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for item in a:
            print(item.replace('\n',''))


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO ao abrir arquivo')
    else:
        try:
            a.write(f'{nome:<30}{idade:>3} anos\n')
        except:
            print('Erro ao cadastrar usuario ')
        else:
            print(f'Usuario {nome} cadastrado com SUCESSO!')
            a.close()