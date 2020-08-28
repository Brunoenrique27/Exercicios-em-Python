termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
laço = 0
termototal = 0
while laço < 10: # enquanto o laço for menor que 10 o termo vai somar com valor da razao
    print(f'{termo} →', end=' ')
    termo += razao
    laço += 1           # soma + 1 dentro do laço
    termototal += 1
print('PAUSA')
novotermo = int(input('Voce quer mostrar mais quantos termos?'))
while novotermo != 0:
    laço = 0
    while laço < novotermo:
        print(f'{termo} →', end=' ')
        termo += razao
        laço +=1
        termototal += 1
    print('PAUSA')
    novotermo = int(input('\nVoce quer mostrar mais quantos termos?'))
print(f'Total de {termototal} termos')
print('FIM')
