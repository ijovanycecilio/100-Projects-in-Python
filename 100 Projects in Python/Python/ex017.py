"""Exercício Python 17: Faça um programa que leia o comprimento do 
cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa."""

#first method

catoposto=float(input('What is the cateto oposto:'))
catadjacente=float(input('What is the cateto adjacente:'))
hipotenusa= ((catadjacente**2)+(catoposto**2))**(1/2)

print('Para o triangulo com catoposto {} e catadjcente {} a hipotenusa é {}'.format(catoposto,catadjacente,hipotenusa))

# second method

import math

hi=math.hypot(catadjacente,catoposto)

print(hi)

