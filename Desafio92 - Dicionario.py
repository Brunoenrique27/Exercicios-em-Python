## Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
dados = {}
dados['nome'] = str(input('Nome:'))
nasc = int(input('Ano de Nascimento:'))
dados['nascimento'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem):'))
if dados['ctps'] == 0:
    print('-='*30)
    for p, v in dados.items():
        print(f'{p} tem o valor {v}')
    quit()
dados['contrato'] = int(input('Ano de contratação:'))
dados['salario'] = float(input('Salário:'))
dados['aposentadoria'] = (dados['contrato'] + 35) - nasc
print('-='*40)
for p, v in dados.items():
    print(f'{p} tem o valor {v}')