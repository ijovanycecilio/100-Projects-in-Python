"""Exercício Python 23: Faça um programa que leia um número 
de 0 a 9999 e mostre na tela cada um dos dígitos separados."""

# forma númerica

num=int(input('write a number between 0 and 9999: '))

milhar=int(num/1000)
centena=int((num-milhar*1000)/100)
dezena=int((num-milhar*1000- centena*100)/10)
unidade=int((num-milhar*1000- centena*100- dezena*10)/1)

print('unidade:{}'.format(unidade))
print('dezena:{}'.format(dezena))
print('centena:{}'.format(centena))
print('milhar:{}'.format(milhar))

# forma com string (it will only work if the user type 4 caracters)

n=str(num)

print('unidade:{}'.format(n[3]))
print('dezena:{}'.format(n[2]))
print('centena:{}'.format(n[1]))
print('milhar:{}'.format(n[0]))

