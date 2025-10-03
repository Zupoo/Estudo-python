produto = int(input('Digite o preço que foi vendido : '))
desconto = int(input('era quanto % do q ele havia pago? : '))
lucro = int(input('Quanto % de lucro ele queria ?'))
desconto = desconto / 100
lucro = lucro /100
a = produto / desconto
a = (a * lucro) + a
print(f'{a:.1f}')
