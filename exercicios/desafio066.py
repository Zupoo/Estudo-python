# soma = 0
# cont = 0
# while True:
#     n = int(input('Digite um numero , se quiser parar digite 999 : '))
#     if n == 999:
#         break
#     soma = soma + n
#     cont = cont + 1
# print(f'A soma dos {cont} numeros digitados é {soma}')

soma = 0
cont = 0
n = int(input('Digite um numero : '))
while True:
    soma = soma + n
    cont = cont + 1
    n = int(input('Digite outro numero , se quiser parar digite 999 : '))
    if n == 999:
        break
print(f'A soma dos {cont} numeros digitados é {soma}')