"""Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por 
um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

days=float(input("How many days?"))
km=float(input('How many km were run?'))

price=(days*60.0 + km*0.15)

print('The final price is {}'.format(price))
