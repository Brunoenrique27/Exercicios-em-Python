print('Leia o ano de nascimento de sete pessoas, e mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores')
import datetime
anoatual = datetime.date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input(f'Em que ano a {c}º pessoa nasceu?'))
    idade = anoatual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas ja sao de maior')
print(f'{menor} pessoas sao de menor idade')
