print("""Pergunte a distancia de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 POR Km para viagens ate 200km e R$0,45 para viagens mais longas.""")

dis = float(input('Quantos km voce percorreu? '))
calc1 = dis*0.50
calc2 = dis*0.45
if dis <=200:
    print(f'Sua viagem foi de {dis}kms e voce pagara R$0,50 por km percorrido, totalizando R${calc1:.2f} reais')
else:
    print(f'Você pagara R${calc2:.2f} reais por km pois ultrapassou de 200km ')
