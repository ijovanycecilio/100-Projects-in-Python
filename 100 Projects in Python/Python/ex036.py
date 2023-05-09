"""Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário 
para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e 
em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário 
ou então o empréstimo será negado."""

value_house=float(input("How much is the house?"))
salary_buyer=float(input('How much is your salary?'))
years=int(input('HOw many years you will pay?'))

prestacao=value_house/years

if prestacao*0.3 >= salary_buyer:
    print('O emprestimo foi negado!')

else:
    print('Parabéns,seu emprestimo foi aprovado!')