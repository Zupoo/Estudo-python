lista =[ [], [] ]
for c in range (0, 7):
    n = int(input(f'Digite o {c+1}. valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-='*33)
lista[0].sort()
print(f'Os valores pares digitados : {lista[0]}')
lista[1].sort()
print(f'Os valores impares digitados : {lista[1]}')
