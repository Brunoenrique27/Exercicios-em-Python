print("""Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar "80 km/h" mostre uma mensagem que ele sera multado
A multa vai custar R$7,00 por cada Km acima do limite""")

velo = float(input('Qual sua velocidade? '))
multa = (velo-80) *7.00
if velo > 80:
    print(f'Sua velocidade foi de {velo}km/h e voce foi multado')
    print(f'Sua multa sera de {multa} reais por km excedido')
else:
    print('Parabens voce não foi multado')