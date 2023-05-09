"""Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e 
mostre na tela a sua porção Inteira."""


# fist method 

import math

number=float(input('Write down a number:'))

print('The number typed was {} and its int part is {}'.format(number,math.trunc(number)))

# second method 

from math import trunc

number=float(input('Write down a number:'))

print('The number typed was {} and its int part is {}'.format(number,trunc(number)))

# third method 


number=float(input('Write down a number:'))

print('The number typed was {} and its int part is {}'.format(number,int(number)))