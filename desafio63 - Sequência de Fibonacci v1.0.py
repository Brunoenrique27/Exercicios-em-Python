##leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
numero = int(input('Digite um termo:'))
t1 = 0
t2 = 1
t3 = 0
c = 3
print(f'{t1} →{t2}→',end=' ')
while c <= numero:
    t3 = t1 + t2
    print(f'{t3}→ ',end=' ')
    t1 = t2
    t2 = t3
    c +=1
print('FIM')