print('Leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade')
cor = {'vermelho':'\033[31m','azul':'\033[34m','limpa':'\033[m'}
centro =' '*2
import time
import datetime
print(f"""{centro}-Até {cor['vermelho']}9 anos{cor['limpa']}:{cor['azul']}MIRIM\033[m
{centro}-Até {cor['vermelho']}14 anos{cor['limpa']}:INFANTIL\033[m
{centro}-Até {cor['vermelho']}19 anos\033[m:{cor['azul']}JUNIOR\033[m
{centro}-Até {cor['vermelho']}20 anos\033[m:{cor['azul']}SÊNIOR\033[m
{centro}-Acima:{cor['azul']}MASTER\033[m""")
ano = int(input('Digite seu ano de Nascimento e de enter:'))
atual = datetime.date.today().year
idade = atual - ano
print('Vamos definir agora sua categoria abaixo só um instante...')
time.sleep(2)
if idade <= 9:
    print(f'Voce tem {idade} anos, sua categoria é{cor["azul"]} MIRIM\033[m')
elif idade <= 14:
    print(f'Voce tem {idade} anos, sua categoria é{cor["azul"]} INFANTIL\033[m')
elif idade <= 19:
    print(f'Voce tem {idade} anos, sua categoria é{cor["azul"]} JUNIOR\033[m')
elif idade <= 25:
    print(f'Voce tem {idade} anos, sua categoria é{cor["azul"]} SENIOR\033[m')
else:
    print(f'Voce tem {idade} anos, sua categoria é{cor["azul"]} MASTER\033[m')
