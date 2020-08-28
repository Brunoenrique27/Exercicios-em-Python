lista = []
def cadastrar(msg):
    lista.append(msg)

def remover():
    lista.pop()


def tela(nome):
    print(nome)


while True:
    print('1 - Cadastrar\n2 - Remover\n3 - Nada a fazer\n4 - Ver lista')
    op = int(input('Qual opção?'))
    if op == 1:
        cads = cadastrar(str(input('Digite um nome:')))
    elif op == 2:
        remover()
    elif op == 3:
        print('Nada a fazer')
    elif op == '4':
        tela(lista)
    esc = str(input('Quer continuar? S/N:'))
    if esc == 'N':
        break

print(lista)

