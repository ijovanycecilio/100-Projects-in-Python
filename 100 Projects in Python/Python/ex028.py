"""Exercício Python 28: Escreva um programa que faça o computador “pensar” em um 
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o 
número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""


print('---'*20)
num=int(input('Write a number between 0 and 5:'))
print('---'*20)

import random
alet= random.randint(0,5)

import time
print('PROCESSANDO...')

time.sleep(4)

if num==alet:
    print('Você acertou o número')

else:
    print('Você errou!')
print('O número que pensei foi {}'.format(alet))
