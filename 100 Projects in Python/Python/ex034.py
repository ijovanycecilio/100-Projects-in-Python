"""Exercício Python 34: Escreva um programa que pergunte o salário de um 
funcionário e calcule o valor do seu aumento. Para salários superiores 
a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salary=float(input("what is your salary?"))

if salary<= 1250:
    print('Your new salary with 15 percent of increase is {:.2f}'.format(salary*1.15))

else:
    print('Your new salary with 10 percent of increase is {:.2f}'.format(salary*1.10))