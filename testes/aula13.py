# print('Oi')
# print('Oi')
# print('Oi')
for c in range(0,3):
    n = int(input('Digite um numero'))
a = 0
for c in range(0, 6):
    print('oi')
    a = a+1
    print(a, c)
print('fiM')

n = int(input('Vou contar de 0 até o numero q voce escolher : '))
for c in range(0, n+1):

    print(c)

x = int(input('Agora vou contar do numero q voce escolheu até 0: '))
for c in range(x, -1, -1):
    print(c)

inicio = int(input('escolha um numero : '))
fim = int(input('Voce quer q eu conte do numero q voce escolheu até quanto? : '))

if inicio < fim:
    for c in range(inicio, fim+1):
        print(c)
else:
    for c in range(inicio, fim -1 , -1):
        print(c)