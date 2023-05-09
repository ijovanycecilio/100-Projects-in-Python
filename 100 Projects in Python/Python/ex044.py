"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por 
um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros"""

valor_produto=float(input('Qual o valor do produto:'))

print('----'*20)
print('Digite o número de acordo com a opção escolhida')
print('[1]- à vista dinheiro/cheque:')
print('[2]- à vista no cartão:')
print('[3]- em até 2x no cartão:')
print('[4]- 3x ou mais no cartão:')
print('----'*20)

forma_pagamento=int(input('Qual a forma de pagamento:'))

if forma_pagamento==1:
    valor_produto =valor_produto-valor_produto*0.1
    print('O valor do produto a ser pago é {}'.format(valor_produto))

elif forma_pagamento==2:
    valor_produto =valor_produto-valor_produto*0.05
    print('O valor do produto a ser pago é {}'.format(valor_produto))

elif forma_pagamento==3:
    valor_produto =valor_produto
    print('O valor do produto a ser pago é {}'.format(valor_produto))

elif forma_pagamento==4:
    valor_produto =valor_produto+valor_produto*0.2
    print('O valor do produto a ser pago é {}'.format(valor_produto))

