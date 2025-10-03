num1 = int(input('Digite um numero'))
num2 = int(input('Digite outro numero'))
num3 = int(input('Digite mais ou numero'))

maior = num1
menor = num1
meio = 0

# defindndo o maior
if num2 >= num1:
    maior = num2
if num3 >= maior:
    maior = num3

#definindo o menor
if num2 <= num1:
    menor = num2
if num3 <= menor:
    menor = num3

#definindo o do meio
if num1 != maior:
    if num2 != menor:
        meio = num1
if num2 != maior:
    if num2 != menor:
        meio = num2
if num3 != maior:
    if num3 != menor:
        meio = num3

#se tiver numero igual

if meio == 0:
    if num1 == num2:
        meio = num1
    if num1 == num3:
        meio = num1
    if num2 == num3:
        meio = num2

print(maior, meio, menor)

