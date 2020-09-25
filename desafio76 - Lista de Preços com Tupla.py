## Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista = 'lapis', 1.75, 'Borracha', 2.00, 'Caderno',15.90,\
        'Estojo', 25.00,'Transferidor',4.20,'Compasso',9.99,\
        'Mochila',120.32,'Canetas',22.30,'Livro',34.90
print('-'*50)
print(f'{"LISTAGEM DE PREÇO":^50}')
print('-'*50)
for item in range(0, len(lista)):    #mostra o total da lista
    if item % 2 == 0:                  #primeiro numero entre o total dividido por 2 que o resto é 0
        print(f'{lista[item]:.<30}', end=' ')
    if item % 2 !=0:
        print(f'R${lista[item]:>7.2f}')

print(len(lista))