"""Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

num1=float(input('Write number 1:'))
num2=float(input('Write number 2:'))
num3=float(input('Write number 3:'))

# verificando menor

menor=num3

if num1 <= num2 and num1 <= num3:

   menor=num1

if num2 <= num1 and num2 <= num3:
    
    menor=num2
   
print('The number {} is minimum'.format(menor))        

# verificando o maior

maior=num3

if num1 >= num2 and num1 >= num3:

   maior=num1

if num2 >= num1 and num2 >= num3:
    
    maior=num2
   
print('The number {} is maximum'.format(maior))        