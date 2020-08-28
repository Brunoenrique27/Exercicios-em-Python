while True:
    numero = int(input('Qual numero da tabuada voce quer ver?'))
    if numero < 0:
        break
    print('*'*30)
    for c in range(1,11):
        print(f'{numero} x {c} = {numero*c}')
print('PROGRAMA FINALIZADO POIS VC DIGITOU UM NUMERO NEGATIVO...')