import random
num = int(input('O computador pensou em um numero de 0 a 5 , tente adivinhar: '))
numpc = random.randint(0, 5)
print(numpc)
if num == numpc:
    print('Parabens voce acertou !')
else:
    print('Que pena voce perdeu , o numero q o computador pensou foi {}'.format(numpc))
    