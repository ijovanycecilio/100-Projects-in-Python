"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO"""

nota1=float(input('What is your first grade:'))
nota2=float(input('What is your second grade:'))

media=(nota1+nota2)/2

if media <5:
    print('Sua média foi {} e você está reprovado'.format(media))

elif media >=7:
    print('Sua média foi {} e você está aprovado'.format(media))

else:
    print('Sua média foi {} e você está recuperação'.format(media))