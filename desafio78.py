valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-='*30)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor foi {max(valores)} nas posições', end=' ')
for posiçao, num in enumerate(valores):
    if num == max(valores):
        print(f'{posiçao}...', end=' ')
print(f'\nO menor valor foi {min(valores)} nas posiçoes',end=' ')
for posiçao, num in enumerate(valores):
    if num == min(valores):
        print(f'{posiçao}...', end=' ')