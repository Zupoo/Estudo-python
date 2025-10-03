somapar = 0
coluna3 = 0
maior = 0
lista = [], [], []
for lx in range (0,3):
    for n in range (0,3):
        lista[lx].append(int(input(f'Digite um valor para {lx+1}, {n+1} ')))
for linha, numerosdalinha in enumerate(lista):
    if linha == 1:
        maior = numerosdalinha[0]
        for numero2 in numerosdalinha:
            if numero2 > maior:
                maior = numero2
    for coluna, numero in enumerate(numerosdalinha):
        print(f'[ {numero} ]', end = '')
        if numero % 2 == 0:
            somapar = somapar + numero
        if coluna == 2:
            coluna3 = coluna3 + numero
        
    print('')
print('-='*33)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é : {max(lista[1])}')
print(maior)