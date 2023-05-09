"""Exercício Python 51: Desenvolva um programa que leia o primeiro termo 
e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""

print('-/-/-/'*10)
print(' OS 10 PRIMEIROS TERMOS DE UMA PA')
print('-/-/-/'*10)

primeiro=int(input('Primeiro termo:'))
Razão=int(input('Razão:'))

termo=primeiro

for c in range (1,11):
    termo= termo + Razão
    print(termo,end=' ')

print('Fim')