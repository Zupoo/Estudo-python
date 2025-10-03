num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

maior = num1
menor = num1
meio = 0

# Definindo o maior
if num2 >= maior:
    maior = num2
if num3 >= maior:
    maior = num3

# Definindo o menor
if num2 <= menor:
    menor = num2
if num3 <= menor:
    menor = num3

# Definindo o do meio sem usar and ou or
if num1 != maior:
    if num1 != menor:
        meio = num1
if num2 != maior:
    if num2 != menor:
        meio = num2
if num3 != maior:
    if num3 != menor:
        meio = num3

# Se o meio não foi definido, verificar números iguais
if meio == 0:
    if num1 == num2:
        meio = num1
    if num1 == num3:
        meio = num1
    if num2 == num3:
        meio = num2
    # Se todos são iguais
    if num1 == num2 and num2 == num3:
        meio = num1  # Pode ser qualquer um

print(f'Menor: {menor}, Meio: {meio}, Maior: {maior}')
