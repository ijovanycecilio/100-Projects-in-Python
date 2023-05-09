"""Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente."""

name=str(input('Write your full name:')).strip()

name=name.split()


print(name[0],name[len(name)-1])