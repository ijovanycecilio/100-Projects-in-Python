""" Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na 
tela o seu sucessor e seu antecessor."""

number=int(input('Type a number, please:'))

antecessor=number-1
sucessor=number+1

print('Para o número {} o antecessor é {} e o Sucessor {}'.format(number, antecessor,sucessor))
print('Para o número {} o antecessor é {} e o Sucessor {}'.format(number, (number-1),(number+1)))
