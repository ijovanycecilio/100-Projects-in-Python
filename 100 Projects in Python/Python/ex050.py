"""Exercício Python 50: Desenvolva um programa que leia seis números 
inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""

soma=0
cont=0

for c in range (1,7):
    num=float(input('Write a number:'))
    if num%2 ==0:
        soma=soma+num
        cont=cont+1

print( 'Foram digitados {} números pares e a soma deles é {}'.format(cont,soma))
