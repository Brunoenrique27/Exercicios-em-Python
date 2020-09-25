## Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Nome do Aluno:'))
aluno['media'] = float(input(f'Media de {aluno["nome"]}:'))
if aluno["media"] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situaçao'] = 'Recuperação'
else:
    aluno['situaçao'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f' {k} é igual {v}')