# n1 = int(input('Digite um numero'))
# n2 = int(input('Digite outro numero'))
# n3 = int(input('Digite outro numero'))
# n4 = int(input('Digite outro numero'))

# tupla = (n1, n2, n3, n4)
tupla = ()
for c in range(0,4):
    print(c)
    n = int(input('Digite um numero : '))
    tupla = tupla + (n,)
print(tupla)
cont = 0
par = 0
pares = ()
for n in tupla:
    if n == 9:
        cont = cont + 1
    if n % 2 == 0:
        par = par + 1
        pares = pares + (n,)
print(f'O numero 9 apareceu { cont} vezes')
if 3 in tupla:
    print(f'O primeiro numero 3 digitado foi o {tupla.index(3) + 1}º numero')
else:
    print('O valor 3 nao foi digitado em nenhum aposição')
print(f'Dos numeros digitados {par} são par , os {pares}')
