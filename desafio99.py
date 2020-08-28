from random import randint
from time import sleep
def maior():
    tot = randint(1,6)
    c = 0
    while c <= tot:
        print('-='*30)
        print('Analisando os valores passados...')
        quant = randint(1, 10)
        lista = []
        for v in range(1,quant+1):
            v = randint(1,10)
            print(f'{v}',end=' ')
            sleep(0.4)
            lista.append(v)
        print(f'Foram informados {quant} valores.')
        print(f'O maior valor informado foi {max(lista)} ')
        c += 1

maior()