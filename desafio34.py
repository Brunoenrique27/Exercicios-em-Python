print('Pergunte o salario de um funcionario e calcule o valor do seu aumento.')
print('Para salarios superiores a R$1.250,00, o aumento sera de 10%')
print('Para os inferiores ou iguais, o aumento é de 15%')

salario: float = float(input('Qual é o seu salario? '))
if salario <= 1250:
    print(f'Seu aumento sera de 15% seu salario sera de R${(salario*15/100) + salario:.2f} reais.')
else:
    print(f'Seu aumento sera de 10% seu salario de R${(salario*10/100) + salario:.2f} reais.')