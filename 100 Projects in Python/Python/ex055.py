"""Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final,
 mostre qual foi o maior e o menor peso lidos."""



peso= float(input('What is the weight of {} ª person:').format(1))
maior=peso
menor=peso

for c in range(1,5):
    peso=float(input('What is the weight of {} ª person:').format(c))

    if peso>maior:
        maior=peso

    elif peso < menor:
        menor=peso

print('O maior peso é {} e o menor é {}'.format(maior,menor))
    
 