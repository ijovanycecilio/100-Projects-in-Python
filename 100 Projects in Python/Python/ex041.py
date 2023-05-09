"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER"""

from datetime import date

year_atual= date.today().year
year_nasc= int(input('What year did you born?'))

age= year_atual-year_nasc

print(year_atual)
print(age)

if age<9:
    print(' Sua categoria é Mirin')

elif age<=14:
    print('Infantil')

elif age<=19:
    print('junior')

elif age<=25:
    print('Senior')

elif age > 25:
    print('Master')