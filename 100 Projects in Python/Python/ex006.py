"""Exercício Python 006: Crie um algoritmo que leia um número e 
mostre o seu dobro, triplo e raiz quadrada."""

number=int(input("Type a number:"))

dobro=number*2
triplo=number*3
raizquadrada=pow((number),(1/2))

print('Para o número {} o dobre é {}, triplo {} e a raiz quadrada é {}'.format(number,dobro,triplo,raizquadrada))