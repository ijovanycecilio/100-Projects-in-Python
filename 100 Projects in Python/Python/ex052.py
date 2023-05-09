"""Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num=int(input('Digite um número:'))

primo=0

for c in range (1,num+1):
    if num%c==0:
        primo=primo+1
        print('\033[33m', end=' ')
    else:
        print('\033[34m', end=' ')
    print('{}'.format(c), end=' ')

if primo>2:
        print('O número não é primo:')

else:
        print('\nO número é primo:')
