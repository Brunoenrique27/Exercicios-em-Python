from time import sleep
def contador(inicio, fim , passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):       # Programa inicia do menor para o maior
            print(f'{c}', end=' ')
            sleep(0.4)
        print('FIM!')
    if inicio > fim:
        for c in range(inicio, fim - 1, -passo):         # Programa inicia do maior para o menor
            print(f'{c}', end=' ')
            sleep(0.4)
        print('FIM')
contador(1,10,1)
contador(0,10,2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
contador(inicio, fim, passo)
