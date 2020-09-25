print('''leia o nome, idade, sexo, de 4 pessoas e no final mostre
-A media de idade do grupo
-Qual é o nome do homem mais velho.
-Quantas mulheres tem menos de 20 anos.''')
soma = 0
media = 0
maisvelho = 0
velho = ''
totmu20 = 0
for c in range (1,5):
    print(f'---- {c}º PESSOA ----')
    nome = str(input(f'Qual seu NOME:'))
    idade = int(input(f'Qual é sua idade:'))
    sexo = str(input(f'Qual seu sexo [M/F]:')).upper()
    soma += idade  # aqui soma a idade de todos
    media = soma / c  # aqui tira a media
    if c == 1 and sexo == 'M':   #aqui no primeiro laço define quem é o mais velho e o nome do mais velho
        maisvelho = idade
        velho = nome
    if sexo == 'M' and idade > maisvelho: #aqui verifica se o sexo for 'M' e a idade dele for maior que a idade do mais velho do primeiro laço
        maisvelho = idade
        velho = nome
    if sexo == "F" and idade < 20: #verifica quantas mulheres menor de 20 anos
        totmu20 += 1

print(f'A media de idade é {media} e o homem mais velho é {velho} com {maisvelho}')
print(f'Tem apenas {totmu20} mulheres abaixo de 20 anos')
