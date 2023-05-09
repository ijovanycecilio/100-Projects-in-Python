"""Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na 
tela o valor do seno, cosseno e tangente desse ângulo."""

import math

angle=float(input("Write down an angle:"))

seno=math.sin(math.radians(angle))
cosseno=math.cos(math.radians(angle))
tangente=math.tan(math.radians(angle))

print(seno,cosseno,tangente)

