"""Exercício Python 7: Desenvolva um programa que 
leia as duas notas de um aluno, calcule e mostre a sua média."""

nota1=float(input("Type the first grade:"))
nota2=float(input("Type the second grade:"))

media=(nota1+nota2)/2

print('A média entre as notas {:.1f} e {:.1f} é {:.2f}'.format(nota1,nota2,media))
