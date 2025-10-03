# 50 20 10 e 1
sacar = int(input('Quanto voce quer sacar? : '))
cinquenta = 0
vinte = 0
dez = 0
um = 0
while sacar >= 50:
    sacar = sacar - 50
    cinquenta = cinquenta + 1
while sacar >= 20:
    sacar = sacar - 20
    vinte = vinte + 1
while sacar >= 10:
    sacar = sacar - 10
    dez = dez + 1
while sacar >= 1:
    sacar = sacar - 1
    um = um + 1

print('Total de cedulas')
if cinquenta > 0:
    print(f'{cinquenta} notas de 50 reais')
if vinte > 0 :
    print(f'{vinte} notas de 20 reais')
if dez > 0:
    print(f'{dez} notas de 10 reais')
if um > 0:
    print(f'{um} notas de 1 real')