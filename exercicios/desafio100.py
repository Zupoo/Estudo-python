import random
import time

def sorteio(lista):
    print('Valores sorteados : ', end = '')
    for c in range(0,5):
        time.sleep(0.33)
        lista.append(random.randint(0,10))
        print(f'{lista[c]}', end = ' ', flush = True)
    

def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma = soma + c
    print(f'A soma dos numeros pares da lista é {soma}')

lista = []
print(lista)
sorteio(lista)
print('')
somapar(lista)