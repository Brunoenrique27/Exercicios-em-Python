print('Leia 3 lados e diga se pode formar um triangulo e mostre se o triangulo é equilatero, isósceles ou escaleno')
lado1 = float(input('Digite o primeiro lado e de enter:'))
lado2 = float(input('Digite o segundo lado e de enter:'))
lado3 = float(input('Digite o terceiro lado e de enter:'))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Pode se formar um \033[32mTRIANGULO\033[m')
    if lado1 == lado2 == lado3:
        print('ele é um triangulo \033[34mEQUILATERO\033[m')
    elif lado1!= lado2 != lado3 != lado1:
        print('ele é um triangulo \033[35mESCALENO\033[m')
    else:
        print('Ele é um triangulo \033[30mISOCELES\033[m')
else:
    print('Nao pode se formar um \033[31mTRIANGULO ')
