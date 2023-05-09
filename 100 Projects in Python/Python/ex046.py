

import time

contagem=int(input('Digite o número que deseja começar a contagem regressiva:'))


for c in range (contagem,0,-1):
    print(c)
    time.sleep(1)

print('BUm Bum BUM')