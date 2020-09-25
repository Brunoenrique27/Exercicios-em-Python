print('Leia duas nota de um aluno e calcule sua media, e mostre se ele foi\033[31m REPROVADO\033[m ou esta de \033[32mRECUPERAÇÃO\033[m ou foi\033[34m APROVADO\033[m.')
n1 = float(input('Digite sua primeira nota:'))
n2 = float(input(('Digite sua segunda nota:')))
media = (n1+n2)/2

if media <5:
    print(f'Sua média foi {media} e voce foi\033[31m REPROVADO\033[m')
elif media >= 5 and media <6.99:
    print(f'Sua média foi {media} voce esta de \033[1;31;40mRECUPERAÇÃO\033[m')
else:
    print(f'Sua média foi {media} voce esta\033[34m APROVADO.')