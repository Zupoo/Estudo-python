def linha():
    print('-'*33)


def conjunto(texto):
    print('-'*33)
    print(texto)
    print('-'*33)


def teste(texto):
    linha()
    print(texto)
    linha()


def separa(como):
    print('')
    print(como *33)
    print('')


def soma2(a, b):
    s = a + b
    print(f'A soma de {a} + {b} = {s}')

linha()
print('Oi')
linha()

separa('X')

conjunto('OLA')

separa('X')

teste('Oi OLA Tudo bem?')


separa('X')
separa('X')
separa('X')


def soma2(a, b):
    s = a + b
    print(f'A soma de {a} + {b} = {s}')

def soma3(a, b, c):
    s = a+b+c
    print(f'A soma de {a} + {b} + {c} = {s}')


soma2(2, 3)
soma2(b = 2, a = 3)
soma3(1, 2, 3)

separa('X')

def quantidade(*n):
    print(f'Foram passados como parametro {len(n)} numeros')

def somainfinito(* n):
    print(n)
    print(n[0])
    print(n[1])




somainfinito(2, 4, 5, 7)
quantidade(0, 2, 3, 4, 5, 6, 7)


separa('X')
separa('X')

def dobro(lista):
    for i, c in enumerate(lista):
        c = c * 2
        lista[i] = c
    print(lista)

# def dobro(lista):
#     for i, c in enumerate(lista):
#         c = c * 2
#         print(c)
#         print(lista)

# def dobro(lista):
#     for c in range(0,len(lista)):
#         lista[c] = lista[c] *2
#         print(lista[c])
#         print(lista)

def triplo(lista):
    c = 0
    while c < len(lista):
        lista[c] = lista[c] * 3
        c = c + 1
        print(c)
    print(lista)

a = [2, 4, 6, 8, 10]
dobro(a)
triplo(a)