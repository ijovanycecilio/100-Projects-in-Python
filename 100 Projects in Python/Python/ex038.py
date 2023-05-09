"""Exercício Python 038: Escreva um programa que leia dois números inteiros e 
compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais"""

num1=float(input('Write the first number:'))
num2=float(input('Write the second number:'))

if num1>num2:
    print('O primeiro número {} é maior que o segundo {}'.format(num1,num2))

elif num2>num1:
    print('O segundo número {} é maior que o primeiro {}'.format(num2,num1))

elif num2==num1:
    print('O segundo número {} é igual o primeiro {}'.format(num2,num1)) 