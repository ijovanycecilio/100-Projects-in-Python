"""Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando um laço for."""

num=int(input('Qual número deseja ver a tabuada:'))

print('-/-/-/'*10)
for c in range (0,11):
    print(' {} x {} = {}'.format(c,num,c*num))

print('-/-/-/'*10)
