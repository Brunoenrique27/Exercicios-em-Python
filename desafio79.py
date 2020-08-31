## Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = []
while True:
    num = int(input('Digite um valor:'))
    if num not in valores:
        valores.append(num)
        print('Valor cadastrado com Sucesso...')
    else:
        print('Digite novamente valor duplicado...')
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('Quer continuar?[S/N]:')).strip().upper()[0]
    if opçao == 'N':
        break
print(f'Voce digitou {sorted(valores)}')

