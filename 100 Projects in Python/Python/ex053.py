"""Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se 
ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

frase=str(input('Digite uma frase:')).strip().upper()

palavra=frase.split()
junta=''.join(palavra)
separa=''

for letra in range (len(junta)-1,-1,-1):
    separa= separa+ junta[letra]

if junta==separa:
    print('A frase é palíndromo')

else:
    print('A frase não é palíndromo')

