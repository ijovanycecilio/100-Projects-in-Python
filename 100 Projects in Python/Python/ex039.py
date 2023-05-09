"""Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem 
e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa 
também deverá mostrar o tempo que falta ou que passou do prazo."""

# Asking for age
age=int(input('What is your age?'))

if age<18:
    falta=18-age
    print('Ainda falta {} anos para seu alistamento'.format(falta))

elif age==18:
    print('Está na hora de se alistar')

else:
    anosextra=age-18
    print('Já se passaram {} ano do se alistamente, apresente-se imediatamente'.format(anosextra))


# Asking for year of born

from datetime import date

year_atual= date.today().year
year_nasc= int(input('What year did you born?'))

age= year_atual-year_nasc

if age<18:
    falta=18-age
    print('Ainda falta {} anos para seu alistamento'.format(falta))

elif age==18:
    print('Está na hora de se alistar')

else:
    anosextra=age-18
    print('Já se passaram {} ano do se alistamente, apresente-se imediatamente'.format(anosextra))

