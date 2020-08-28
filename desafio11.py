print('Vamos calcular a area de uma parede(em metros quadrados) para saber quando de tinta sera necessaria? ')
alt = float(input('Quanto de altura mede a parede? '))
larg = float(input('Quanto de largura mede a parede? '))
area = alt*larg
tinta = area/2
print(f'Sua parede tem dimensão de {alt}x{larg} e sua area é de {area}m²')
print(f'Serão necessario {tinta} litros de tinta')