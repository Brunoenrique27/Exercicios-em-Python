print('Digite um nome completo e mostre em seguida o primeiro e o ultimo nome separadamente')
print('Exemplo: Ana Maria de souza, primeiro = Ana, ultimo = Souza')
nome = str(input('Digite seu nome completo ')).strip()
lista = nome.split()

print(f'O primeiro nome é {lista[0]}')
print(f'O ultimo nome é {lista[-1]}')
