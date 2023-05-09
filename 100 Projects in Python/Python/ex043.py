"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura 
de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida"""

peso=float(input('Qual o peso?'))
altura=float(input('Qual a altura?'))

IMC=peso/(altura*altura)

if IMC< 18.5:
    print('Abaixo do peso')
    print('Seu IMC é {}'.format(IMC))

elif IMC <=25:
    print('Peso ideal')
    print('Seu IMC é {}'.format(IMC))

elif IMC <=30:
    print('Sobrepeso')
    print('Seu IMC é {}'.format(IMC))

elif IMC <=40:
    print('Obeso')
    print('Seu IMC é {}'.format(IMC))

elif IMC > 40:
    print('Obesidade Mórbida')
    print('Seu IMC é {}'.format(IMC))