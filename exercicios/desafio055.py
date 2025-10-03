
for c in range(0, 5):
    peso = float(input('Digite um peso em kg'))
    if c == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi de {:.1f}kg e o menor de {:.1f}kg'.format(maior , menor))

