num = int(input('Digite um numero para saber o fatorial dele : '))
contador = num
resultado = 1
print('{}! = '.format(num), end ='')
while contador != 0:
    if contador == 1:
        print(contador, end = '')
        resultado = resultado * contador
        contador = contador - 1
    else:
        print('{} x '.format(contador), end = '')
        resultado = resultado * contador
        contador = contador - 1
print(' = ', resultado)

r = 1
for c in range (1 , num+1):
    r = r * c
    print(r)

print(r)