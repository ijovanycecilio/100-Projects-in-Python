"""Exercício Python 12: Faça um algoritmo que leia o preço 
de um produto e mostre seu novo preço, com 5% de desconto."""

price=float(input('What is the current price of this product?'))

discount=price-price*0.05

print('The new price for this discount of 5 percent if {:.2f}'.format(discount))