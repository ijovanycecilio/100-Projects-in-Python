"""Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário 
e mostre seu novo salário, com 15% de aumento."""

salary=float(input('What is the current salary ?'))

newsalary=salary+salary*0.15

print('The new salary for this increase of 15 percent if {:.2f}'.format(newsalary))