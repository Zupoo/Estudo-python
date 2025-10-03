import random
cont = 1
pc = random.randint(0,10)
print(pc)
lista = [0,1,2,3,4,5,6,7,8,9,10]

print(lista)

n = int(input('O computador pensou em um numero de 0 a 10 , tente advinhar : '))

while pc != n:
    if n in lista:
        cont = cont + 1
        if n > pc:
            n = int(input('Tente um numero menor'))
        elif n < pc :
            n = int(input('Tente um numero maior'))
    else:
        print('A resposta deve ser um numero entre 0 e 10 e isso nao contou como uma tentativa')
        n = int(input('Tente novamente : '))
print('Você acertou e precisou de {} tentativas.'.format(cont))