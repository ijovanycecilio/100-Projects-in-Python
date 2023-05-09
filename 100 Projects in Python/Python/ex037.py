"""Exercício Python 37: Escreva um programa em Python que leia um número 
inteiro qualquer e peça para o usuário escolher qual será a base de 
conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

num=int(input('write a number:'))

print('---'*20)
print('Type one option para convert your number:')
print('[1]-Binário')
print('[2]-Octal')
print('[3]-Hexadecimal')
print('---'*20)

choise=int(input('What is your choise?'))

if choise==1:
    print('O número {} convertido para binário é {}'.format(num,bin(num)))

elif choise==2:
     print('O número {} convertido para Octal é {}'.format(num,oct(num)))

else:
    print('O número {} convertido para Hexagonal é {}'.format(num,hex(num)))