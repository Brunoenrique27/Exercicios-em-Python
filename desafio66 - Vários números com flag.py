cont = soma = 0
while True:
    n = int(input('Digite um valor [999 para sair]:'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Voce digitou {cont} valores e a soma foi {soma}')