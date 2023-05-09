"""Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome."""

name=str(input('Write your name please:')).strip()

print('Analyzing your name')
print("Quantas letras ao todo (sem considerar espaços):{}".format(len(name)))
print('O nome com todas as letras maiúsculas: {}'.format(name.upper()))
print('O nome com todas as letras minúsculas: {}'.format(name.lower()))

separa=name.split()

print('O seu primeiro nome é {} e possui {} letras'.format(separa[0],len(separa[0])))