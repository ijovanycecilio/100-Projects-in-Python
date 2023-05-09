"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o 
recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes"""

r1=float(input('Write the first number:'))
r2=float(input('Write the second number'))
r3=float(input('Write the third number'))

a='Impossível'

if r3 < r1+r2 and r1 < r2+r3 and r2 < r3+r1:
    a='Possível'
    

print('Com os valores {},{} e {}'.format(r1,r2,r3))
print('{} formar o triângulo'.format(a))

if a=='Possível' and r1==r2==r3:
    print('Triangulo Equilatero')

elif a=='Possível' and r1==r2 or r1==r3 or r2==r3:
    print('Triangulo ISÓSCELES')

else:
    print('Triangulo ESCALENO')
