import math

a = int(input('Digite o A da equiacao: '))
b = int(input('Digite o B da equiacao: '))
c = int(input('Digite o C da equiacao: '))


delta = (b*b) - 4*a * c
print(delta)
if delta >= 0:
    raiz_positiva = (-b + math.sqrt(delta))/2*a
    raiz_negativa = (-b - math.sqrt(delta))   /2*a
    # raiz_negativa = (-b - math.sqrt(delta))   /2*a

    print(f'Raizes : {raiz_positiva}, {raiz_negativa}')
else:
    print('Essas sao raizes complexas')

