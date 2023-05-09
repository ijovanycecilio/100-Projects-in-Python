"""Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

import random

name1= str(input('Write a name:'))
name2= str(input('Write a name:'))
name3= str(input('Write a name:'))
name4= str(input('Write a name:'))

lista=[name1,name2,name3,name4]

escolhido=random.choice(lista)

print(escolhido)