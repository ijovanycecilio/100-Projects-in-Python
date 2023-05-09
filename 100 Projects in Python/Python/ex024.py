"""Exercício Python 24: Crie um programa que leia o nome de uma cidade 
diga se ela começa ou não com o nome “SANTO”."""

name_city=str(input('Write the name of the city:')).strip()

name_city=name_city.split()

print('The name of the city starts with SANTOS:')
print(name_city[0].upper()=='SANTOS')