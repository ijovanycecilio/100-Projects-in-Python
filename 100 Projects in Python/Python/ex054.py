"""Exercício Python 54: Crie um programa que leia o ano de nascimento 
de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a 
maioridade e quantas já são maiores."""

from datetime import date

ano_atual=date.today().year
idade=0
cont=0
cont2=0


for c in range (1,8):
    ano=int(input('Qual o ano de nascimento da {} pessoa:'.format(c)))
    idade=ano_atual-ano

    if idade<18:
        cont=cont+1
    
    else:
        cont2=cont2+1

print ('Das 7 pessoas {} já atingiram maioridade penal e {} ainda não'.format(cont2,cont))
