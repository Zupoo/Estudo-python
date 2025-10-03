maior = menor = 0
continuar = ''
lista = []
add = []
cont = 0
while True:
    add.append(input('Nome: '))
    peso = (float(input('Peso:')))
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    add.append(peso)
    lista.append(add[:])
    add.clear()
    cont = cont + 1
    while True:
        continuar = input('Quer registrar mais alguem na lista? [S/N]: ').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break

    if continuar == 'N':
        break
print(f'Aqui esta a lista {lista} , foram adicionados {cont} pessoas a lista')
print(f'O maior peso foi de {maior}kg ', end = '')
for c in lista:
    if c[1] == maior:
        print(f'{c[0]} ', end = '')
print('')
print(f'O menor peso foi de {menor}kg ', end = '')
for c in range(0,len(lista)):
    if lista[c][1] == menor:
        print(f'{lista[c][0]}', end = '')
