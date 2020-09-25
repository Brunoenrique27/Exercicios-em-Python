#validando uma expressão
inicio = final = 0
expre = str(input('Digite a expressão:'))
for c in expre:
    if c == "(":
        inicio += 1
    if c == ")":
        final += 1
if inicio == final:
    print('Sua expressao é valida')
else:
    print('Expressao invalida')