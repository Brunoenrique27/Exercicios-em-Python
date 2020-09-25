print('LOCALIZA ALUGUEIS DE CARROS')
print(input('Qual carro deseja alugar? '))
dia = int(input('Por quantos dias deseja alugar esse carro? '))
km = float(input('Quantos km deseja rodar com esse carro? '))
loc = 60*dia
kmfin = km*0.15
print(f'O custo do seu carro final calculado o valor de 60 por dia sera de R${loc} reais.\n ja o valor referente a {km}km rodados por voce, tera um custo de R${kmfin} reais.')
print(f'o custo total seu sera de R${loc+kmfin} reais.')