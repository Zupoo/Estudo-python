import math
n = int(input('Digite um numero'))
base = int(input('Digite 1 para o numero ser convertido para binário , 2 para octal e 3 para hexadecimal'))

if base == 1: 
    resultado = []
    resto = n % 2
    aux = n//2
    resultado = resultado + [resto]
    if aux != 0:
        resto = aux % 2
        aux = aux // 2
        resultado = resultado + [resto]
    if aux != 0:
        resto = aux % 2
        aux = aux // 2
        resultado = resultado + [resto]
    if aux != 0:
        resto = aux % 2
        aux = aux // 2
        resultado = resultado + [resto]
    if aux != 0:
        resto = aux % 2
        aux = aux // 2
        resultado = resultado + [resto]
    if aux != 0:
        resto = aux % 2
        aux = aux // 2
        resultado = resultado + [resto]
    if aux != 0:
        resto = aux % 2
        aux = aux // 2
        resultado = resultado + [resto]
    if aux != 0:
        resto = aux % 2
        aux = aux // 2
        resultado = resultado + [resto]
    if aux != 0:
        resto = aux % 2
        aux = aux // 2
        resultado = resultado + [resto]
    if aux != 0:
        resto = aux % 2
        aux = aux // 2
        resultado = resultado + [resto]
    if aux != 0:
        resto = aux % 2
        aux = aux // 2
        resultado = resultado + [resto]
    resultado.reverse()
    print(resultado)
        
elif base == 2:
    resultado = []
    aux = n // 8
    resto = n % 8
    resultado = resultado + [resto]

    if aux != 0:
        resto = aux % 8
        aux = aux //8
        resultado = resultado + [resto]

    if aux != 0:
        resto = aux % 8
        aux = aux //8
        resultado = resultado + [resto]

    if aux != 0:
        resto = aux % 8
        aux = aux //8
        resultado = resultado + [resto]

    if aux != 0:
        resto = aux % 8
        aux = aux //8
        resultado = resultado + [resto]

    if aux != 0:
        resto = aux % 8
        aux = aux //8
        resultado = resultado + [resto]

    if aux != 0:
        resto = aux % 8
        aux = aux //8
        resultado = resultado + [resto]

    if aux != 0:
        resto = aux % 8
        aux = aux //8
        resultado = resultado + [resto]

    if aux != 0:
        resto = aux % 8
        aux = aux //8
        resultado = resultado + [resto]

    resultado.reverse()
    print(resultado)

elif base == 3:
    n = hex(n)
    n = n.replace('0x', '')
    print(n)
else:
    print('Não tem essa opção')
    a = oct(83)
    print(a[2:])




