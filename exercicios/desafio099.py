import random
import time
def maior(*n):
    print('Valores: ', end = '')
    for c in n:
        print(c, end = ' ',flush=True)
        time.sleep(0.25)
    if not n:# é a mesma coisa de escrever if len(n) == 0 , é uma forma de descobrir se algo esta vazio 
        print(f'Foram informados {len(n)} valores ao todo')
    else:
        maior = n[0]
        for c in range(1, len(n)):
            if n[c] > maior:
                maior = n[c]
        print(f'Foram informados {len(n)} valores ao todo e o maior é {maior}')

def distancia():
    print('')
    print('-='*20)
    print('')


distancia()
maior(random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
distancia()
maior(random.randint(0,10), random.randint(0,10), random.randint(0,10))
distancia()
maior(random.randint(0,10), random.randint(0,10))
distancia()
maior(random.randint(0,10))
distancia()
maior()
distancia()