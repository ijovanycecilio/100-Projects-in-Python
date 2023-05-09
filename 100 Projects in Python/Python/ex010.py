"""Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na 
carteira e mostre quantos dólares ela pode comprar."""

money=float(input('HOw much money do you have in your virtual wallet?'))
cotation=5.05

wallet=money*cotation

print('According to the cotation today you have in your wallet {}'.format(wallet))