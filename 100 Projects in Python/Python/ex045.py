"""Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."""

import random
import time

num_computador=random.randint(1,3)

print('-/-/-'*20)
print('Escolha a opção que deseja jogar')
print('[1]-Pedra')
print('[2]-Papel')
print('[3]-Tesoura')
print('-/-/-'*20)

num=int(input('Write a number between 1 and 3:'))

print('\\\\\\'*20)
print('JO')
time.sleep(2)
print('KEN')
time.sleep(2)
print('DÔ')
time.sleep(2)
print('\\\\\\'*20)

if num_computador==num:
    print('Esse foi empate, vamos tentar novamente!')

elif num_computador==1 and num==2:
    print('Você ganhou!')

elif num_computador==1 and num==3:
    print('Você perdeu!')

elif num_computador==2 and num==1:
    print('Você perdeu!')

elif num_computador==2 and num==3:
    print('Você ganhou!')

elif num_computador==3 and num==1:
    print('Você ganhou!')

elif num_computador==3 and num==2:
    print('Você perdeu!')


"""
print('---'*20)
num=int(input('Write a number between 0 and 5:'))
print('---'*20)

import random
alet= random.randint(0,5)

import time
print('PROCESSANDO...')

time.sleep(4)

"""