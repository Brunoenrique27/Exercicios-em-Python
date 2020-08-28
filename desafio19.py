print('Um professor quer sortear um dos seus quatros alunos para apagar o quadro, mostre o nome deles e o nome do escolhido')

'''import random
print('O nome dos alunos sao')
print('1º aluno Bruno')
print('2º aluno Rafaela')
print('3º aluno Priscila')
print('4º aluno Eduardo')
sorteado = random.randint(1,4)
print(f'O aluno numero {sorteado} foi sorteado pra apagar a lousa.')'''

import random
aluno1 = str(input('Nome do primeiro aluno= '))
aluno2 = str(input('Nome do segundo aluno= '))
aluno3 = str(input('Nome do terceiro aluno= '))
aluno4 = str(input('Nome do quarto aluno= '))
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)
print(f'O aluno sorteado foi {escolhido}')