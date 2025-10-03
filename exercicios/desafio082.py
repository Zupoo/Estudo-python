lista = []
while True:
    lista.append(int(input('Digite um numero : ')))
    print(lista)
    while True:
        continuar = input('Quer continuar? : ').upper().strip()
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
listapar = []
listaimpar = []
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        listapar.append(lista[c])
for numero in lista:
    if numero % 2 != 0:
        listaimpar.append(numero)

print(f'lista completa {lista}')
print(f'A lista dos numeros pares é {listapar}')
print(f'A lista dos numeros impares é {listaimpar}')
