nome = input('Crie um algortimo que leia um numero e mostre seu dobro seu triplo e sua raiz quadra')
n1 = int(input('Digite um numero'))
do = n1*2
tri = n1*3
rq = n1**(1/2)
print('O meu numero é {}, seu dobro é {} seu triplo é {} e o valor da raiz quadrada é {:.2f}'.format(n1,do,tri,rq))