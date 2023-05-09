"""Exercício Python 35: Desenvolva um programa que leia o comprimento 
de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

r1=float(input('Write the first number:'))
r2=float(input('Write the second number'))
r3=float(input('Write the third number'))

a='Impossível'

if r3 < r1+r2 and r1 < r2+r3 and r2 < r3+r1:
    a='Possível'
    

print('Com os valores {},{} e {}'.format(r1,r2,r3))
print('{} formar o triângulo'.format(a))