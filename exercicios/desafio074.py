import random
tupla = tuple(random.choices(range(0, 9), k=5))
print(f'Aqui esta a listagem dos numeros -> {tupla}')
menor = tupla[0]
maior = tupla[0]
for c in range(1, len(tupla)):
        if tupla[c] < menor:
            menor = tupla[c]
        if tupla[c] > maior:
            maior = tupla[c]
print(maior , menor)

#outra forma de fazer
maiorr = max(tupla)
print(maiorr)
menorr = min(tupla)
print(menorr)