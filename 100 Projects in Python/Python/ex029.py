"""Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite."""

speed=float(input('What is the speed:'))

if speed <=80:
    print('Parabéns, você está dentro do limite de velocidade')

else:
    multa=(speed-80)*7
    print('Você está acima do limite de velocidade e terá que pagar uma multa de R$ {}'.format(multa))
