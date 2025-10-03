lista = []
for c in range (0, 5):
    n = int(input('Digite um numero : '))
    if c == 0:
        maior = n
        menor = n
        print(f'Lista criada e {n} foi adicionado a lista')
    if n >= maior:
        lista.append(n)
        maior = n
        if c != 0:
            print(f'Foi adicionado no final da lista')
    else:
        for i in range (0, len(lista)):
            if n < lista[i]:
                lista.insert(i, n)
                print(f'O numero {n} foi adicionado na posição {i} da lista')
                break
    
print(f'Os valores digitados em ordem foram : {lista}')