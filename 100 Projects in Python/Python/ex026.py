"""Exercício Python 26: Faça um programa que leia uma frase pelo teclado e 
mostre quantas vezes aparece a letra “A”, em que posição ela aparece a 
primeira vez e em que posição ela aparece a última vez."""

sentence=str(input('Write down a sentence:')).strip()

sentence=sentence.upper()


print('The letter A shows up {} times'.format(sentence.count('A')))
print('the first position where it shows up {}'.format(sentence.find('A')+1))
print('the last position where it shows up {}'.format(sentence.rfind('A')+1))