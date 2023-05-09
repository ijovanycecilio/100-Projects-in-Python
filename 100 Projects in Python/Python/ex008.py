"""Exercício Python 8: Escreva um programa que leia um valor em metros e o 
exiba convertido em centímetros e milímetros."""

metros=float(input('Type how many meters:'))

centimetros=metros*100
milimetros=metros*1000

print('A conversão de {} metros é de {}centimetros e {:.1f} milimetros'.format(metros,centimetros,milimetros))