print('Leia o ano de nascimento de um jovem e informe, de acordo com sua idade')
print('Se ele\033[34m ainda vai se alistar\033[m ao serviço militar.\nSe é a\033[34m hora de se alistar\033[m.\nSe já\033[34m passou do tempo\033[m do alistamento')
bemvindo = 'SEJA BEM VINDO AO SERVIÇO DE ALISTAMENTO'
import datetime
print("*"*50)
print(f'{bemvindo:^50}')
print("*"*50)
ano = int(input('Digite o ano de nascimento e de enter:'))
atual = datetime.date.today().year
idade = atual - ano
if idade < 18:
    print(f'Voce ainda ira se alistar, falta {18-idade} anos pra voce se alistar')
elif idade == 18:
    print('Voce ja pode se alistar')
else:
    print(f'Ja passou do tempo de alistamento voce tem {idade} anos, e ja passou do prazo faz {idade-18} anos, seu alistamento foi em {atual-idade+18}')