"""Exercício Python 25: Crie um programa que leia o nome de 
uma pessoa e diga se ela tem “SILVA” no nome."""

name=str(input('Write down your name:')).strip()

print('Is there SILVA in the name typed?')

print('SILVA' in name.upper())