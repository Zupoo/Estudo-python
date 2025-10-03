import math
n = int(input('Digite um numero'))
print('='*20)
resto = False
raiz = int(math.sqrt(n))
if n < 2:
    print(n,'Não é primo')
elif n == 2:
    print(n, 'É primo')
elif n % 2 == 0:
    print(n, 'Não é primo')
else:
    for c in range(3, raiz+1):
        if c % 2 != 0:
            if n % c == 0:
                resto = True
                break
            else:
                resto = False
    if resto == True :
        print('O numero não é primo!')
    elif resto == False:
        print('O numero é primo!!')
