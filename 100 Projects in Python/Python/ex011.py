"""Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de 
tinta pinta uma área de 2 metros quadrados."""

height=float(input('what is the height?'))
lenght=float(input('What is the lenght?'))

area=height*lenght
litros=area/2.0

print('This wall with {} Height and {} lenght has the {} of area.\n Is necessary {} litros to print this wall '.format(height,lenght,area,litros))