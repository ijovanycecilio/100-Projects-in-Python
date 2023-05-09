"""Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de
 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o 
 nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

nome=''
idade=0
sexo=''
lista_nome=[]

for c in range (0,4):
    lista_nome=[c]=[str(input('Qual o nome da {} ª pessoa:'.format(c)))]

print(lista_nome)