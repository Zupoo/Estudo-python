n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro calor'))
n3 = int(input('Digite mais um valor'))

maior = n1
if n2 > maior and n2 > n3:
    maior = n2
if n3 > maior and n3 > n2:
    maior = n3
print('O maior é : ', maior)

menor = n1

if n2 < menor and n2 < n3:
    menor = n2
if n3 < menor and n3 < n2:
    menor = n3

print('O menor é : ', menor)
