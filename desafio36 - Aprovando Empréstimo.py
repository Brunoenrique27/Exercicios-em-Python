print('Aprovação de emprestimo')
print('O programa vai perguntar o\033[34m valor da casa,\033[m o\033[34m salário\033[m do comprador e em \033[34mquantos anos\033[m ele vai pagar.\033[m')
print('Calcule o valor da prestação mensal, sabendo que ela não pode execeder\033[31m 30%\033[m do salario ou então o empréstimo sera negado.')
salario = float(input('Digite seu salário:'))
casa = float(input('Digite o valor da casa:'))
anos = int(input('Em quantos anos voce deseja pagar? '))
prestaçao = casa / (anos*12)
porsalario = salario*30/100
print(f'O valor da casa é R${casa} ficara em {anos*12} parcelas de R${prestaçao:.2f} reais.')
if prestaçao <= porsalario:
    print('Voce teve o emprestimo CONCEDIDO')
else:
    print('Emprestimo NEGADO!')
