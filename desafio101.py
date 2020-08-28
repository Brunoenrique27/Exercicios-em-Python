def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade >= 16 and idade < 18 or idade > 65:
        return print(f'Voce tem {idade} anos, e seu voto é OPCIONAL.')
    elif idade >= 18:
        return print(f'Voce tem {idade} anos, seu voto é OBRIGATORIO.')
    elif idade < 16:
        return print(f'Voce tem {idade} anos, voto NEGADO.')


ano = int(input('Em que ano voce nasceu? '))
voto(ano)
