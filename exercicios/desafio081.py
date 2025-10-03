lista = []
cont = 0
while True:
    n = int(input('Digite um numero : '))
    lista.append(n)
    cont = cont+1
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = input('Quer continuar? [S/N]').strip().upper()
        print(continuar)
    if continuar == 'N':
        break
print('-='*20)
print(lista)
print('-='*20)
lista2 = lista[:]
lista2.sort(reverse = True)
print(f'A lista do maior para o menor {lista2}')
print(f'Foram digitados {cont} numeros')
if 5 in lista:
    print(f'Tem o numero 5 na lista e é o  {lista.index(5)+1} numero da lista')
    for c in range(lista.index(5)+1, len(lista)):
        if lista[c] == 5:
            print(f'Tem mais 5 na lista e esta na posição {c+1}',end = '')
else:
    print('Não tem numero 5 nessa lista')