import random
import time
lista = []
jogos = []
quantos = int(input('Quantos jogos voce quer q eu sorteie? : '))
qtd = int(input('Quantos numeros voce deseja q tenha em cada jogo?  : '))
menor = int(input('Qual o menor numero q pode ser sorteado? : '))
maior = int(input('Qual o maior numero q pode ser sorteado? : '))
for i in range(0,quantos):
    while len(lista) != qtd:
        num = random.randint(menor, maior)
        if not num in lista:
            lista.append(num)
        else:
            while num in lista:
                num = random.randint(menor, maior)
            lista.append(num)
    jogos.append(lista[:])
    lista.clear()
for c in jogos:
    x = sorted(c)
    time.sleep(2)
    print(x)
        
