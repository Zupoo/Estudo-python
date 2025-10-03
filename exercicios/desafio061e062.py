n = int(input('Informe o primeiro termo'))
razao = int(input('Informe a razao'))
qtdvezes = 10
total = 0
while qtdvezes != 0:
    cont = qtdvezes
    while cont != 0:
        print(n)
        cont = cont - 1
        qtdvezes = qtdvezes -1
        n = n + razao
        total = total + 1
    qtdvezes = int(input('Quer q o programa mostre mais quantos termos?'))
print('PA finalizada e foram mostrados ',total, 'termos')
print('FIM')


# print( total)
# parar = 0
# while parar != 1:
#     print('')
#     maistermos = int(input('Voce quer q o programe mostre mais quantos termos? : '))
#     cont2 = 0
#     if maistermos == 0:
#         parar = 1
#     while cont2 != maistermos:
#         if cont2 == 0:
#             print(n, end = '')
#             n = n + razao
#             cont2 = cont2 + 1
#             total = total + 1
#         else:
#             print('-> ', end = '')
#             print(n, end = '')
#             n = n + razao
#             cont2 = cont2 + 1
#             total = total + 1
# print('Progressão finalizada com {} termos mostrados'.format(total))
        
