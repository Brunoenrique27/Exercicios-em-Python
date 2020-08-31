print('Um professor quer sortear um dos seus quatros alunos para apagar o quadro, mostre o nome deles e o nome do escolhido')

import random
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno:'))
aluno4 = str(input('Nome do quarto aluno:'))
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)
print(f'O aluno sorteado foi {escolhido}')