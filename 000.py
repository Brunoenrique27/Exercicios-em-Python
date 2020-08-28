from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if valor == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1         #aqui faz a contagem dos numeros
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor é {maior}.')


maior(2, 5, 7, 9, 1)
maior(8, 22, 100)
maior(5, 6, 7, 5, 52)
maior(1, 2)
maior()

