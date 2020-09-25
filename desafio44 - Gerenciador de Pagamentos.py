print('Calcule o valor a ser pago por um produto, considerando o seu\033[34m preço normal\033[m e\033[34m condição de pagamento\033[m:')
print('á vista no dinheiro/cheque:\033[31m 10% de desconto\033[m')
print('Á vista no cartão:\033[34m 5% de desconto\033[m')
print('Em até 2x no cartão:\033[34m preço normal\033[m')
print('3x ou mais no cartão:\033[34m 20% de jruos\033[m')
import random
valor = float(input('Digite o valor do produto:'))
print('FORMAS DE PAGAMENTO')
print("""Opção [ 1 ] 10% de desconto
Opção [ 2 ] a vista 5% no cartão
Opção [ 3 ] em até 2x no cartão preço normal
Opção [ 4 ] 3x ou mais 20% de juros""")
pagamento = int(input('Qual opção de pagamento?'))
if pagamento == 1:
    total = valor*10/100+valor
    print(f'Voce pagara a vista com 10% de desconto ficando num valor final de R${total:.2f}')
elif pagamento == 2:
    total = valor*5/100+valor
    print(f'Você pagara a vista com 5% de desconto ficando no valor de R${total:.2f}')
elif pagamento == 3:
    totpar = valor / 2
    total = valor
    print(f'Voce pagara em 2x no cartao com cada parcela no valor de R${totpar}')
elif pagamento == 4:
    total = valor*20/100+valor
    totpar = valor*20/100
    print(f'Voce pagara em 3x com 20% de juros sua parcela sera no valor de R${totpar}')
else:
    pagamento = 0
    total = valor
    print('Opçao invalida de pagamento')
print(f'Sua compra de R${valor} vai custar no final R${total}')
