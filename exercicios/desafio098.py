import time
def linha():
    print('-='*20)


# def cont(a, b):
#     linha()
#     print('Contagem de 1 até 10')
#     for c in range (a,b+1):
#         print(c, end = ' ',flush=True)
#         # time.sleep(0.25)
#     print('')
#     linha()

# def regres(a, b):
#     print('Contagem de 10 até 1')
#     linha()
#     for c in range(a,b-1 , -1):
#         print(c, end = ' ',flush=True)
#         # time.sleep(0.25)
#     print('')
#     linha()


def contp(i, f, p):
    print(f'Contagem de {i} até {f} ', end = '')
    if p != 1:
        print(f'pulando de {p} em {p}')
    else:
        print('')
    while True:
        if p == 0:
            p = 1
        if i < f:
            f = f+1
            if p < 0:
                p = (p) * (-1)
            for c in range (i, f, p):
                print(c, end = ' ',flush=True)
                time.sleep(0.25)
            break
        elif i > f:
            if p > 0:
                p = p * -1
            f = f -1
            for c in range (i, f, p):
                print(c, end = ' ',flush=True)
                time.sleep(0.25)
            break

linha()
contp(1,10,1)
print('')
linha()
contp(10,1,1)
print('')
linha()
print('Sua vez de presonalizar a contagem!')
inicio = int(input('Inicio : '))
fim = int(input('Fim : '))
passo = int(input('Passo : '))
contp(inicio, fim, passo)
print('')
linha()
