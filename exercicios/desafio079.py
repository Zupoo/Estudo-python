lista = []
continuar = ''
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar a lista ')
    else:
        lista.append(n) 
        print('Valor adicionado')
    while True: 
        continuar = input(('Quer continuar? [S/N]')).strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
    print(lista)
print(f'A os valores digitados em ordem crescente ficaram assim : {sorted(lista)}')
