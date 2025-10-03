# lista = []
# for c in range (0, 5):
#     n = int(input('Digite um numero para ser adicionado na lista'))
#     if c == 0:
#         maior = n
#         menor = n
#         lista.append(n)
#         print(f'{n} Foi adicionado na lista')
#     if n > maior:
#         lista.append(n)
#         maior = n
#     elif n < menor:
#         list.insert(0, n)
#         menor = n
    
# lista = []
# for c in range (0, 5):
#     n = int(input('Digite um numero para ser adicionado na lista'))
#     if c == 0:
#         lista.append(n)
#         maior = n
#         menor = n
#     if c == 1:
#         if n > maior:
#             lista.append(n)
#             maior = n
#         if n < menor:
#             lista.insert(0, n)
#             menor = n
#     else:
#         for i in range(0, len(lista)):
#             if n <= lista[i] and n >= lista[i -1]:
#                 lista.insert(i, n)
#                 print(lista,'a')
#                 break
# print(lista)

lista = []
add = 0
for c in range (0, 5):
    n = int(input('Digite um numero para ser adicionado na lista'))
    add = 0
    if c == 0:
        lista.append(n)
        add = 1
    else:
        for i in range(0, len(lista)):
            if n <= lista[i]:
                lista.insert(i, n)
                add = 1
                break
    if add == 0:
        lista.append(n)
print(lista)