"""Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

import random

name1= str(input('Write a name:'))
name2= str(input('Write a name:'))
name3= str(input('Write a name:'))
name4= str(input('Write a name:'))

lista=[name1,name2,name3,name4]

random.shuffle(lista)

print(lista)