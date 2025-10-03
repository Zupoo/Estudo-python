n1 = int(input('Digite comprimento de 1 lado do triangulo : '))
n2 = int(input('Digite comprimento de outro lado do triangulo : '))
n3 = int(input('Digite o comprimento do ultimo lado do triangulo : '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('É possivel formar um triangulo com esses seguimentos de reta.')
    if n1 == n2 == n3:
        print('Esse triangulo é equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Esse triangulo é isósceles')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('Esse triangulo é Escaleno')
else:
    print('Não é possivel formar um triangulo com esses 3 seguimentos de reta')