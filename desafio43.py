print('Calculo do IMC')
print('Abaixo de 18.5:\033[31m ABAIXO DO PESO\033[m')
print('Entre 18.5 e 25:\033[34m PESO IDEAL\033[m')
print('\033[35m25\033[m até\033[34m 30\033[m:SOBREPRESO')
print('\033[35m30\033[m até\033[35m 40\033[m:OBESIDADE')
print('Acima de \033[34m40\033[m: OBESIDADE MORBIDA\033[m')

peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso/(altura*altura)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f} voce esta ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é de {imc:.2f} você esta no PESO IDEAL')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.2f} voce esta SOBRE PRESO')
elif imc >= 30 and imc <= 40:
    print(f'Seu IMC é de {imc:.2f} voce esta num estagio de OBESIDADE')
else:
    print(f'Seu IMC é de {imc:.2f} voce esta num estagio de OBESIDADE MORBIDA')