lista = [], [], []
for lx in range (0,3):
    for n in range (0,3):
        lista[lx].append(input(f'Digite um valor para {lx+1}, {n+1} '))
for linha in lista:
    for numero in linha:
        print(f'[ {numero:^5}]', end = '')
    print('')
print('-='*33)
for c in lista:
    for a in range(0,3):
        print(f'[ {c[a]} ]', end = '')
    print('')