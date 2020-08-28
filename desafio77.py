palavra = 'aprender','programar', 'linguagem', 'estudar','futuro'
for item in palavra:
    print(f'\nNa palavra {item.upper()} temos', end=' ')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
