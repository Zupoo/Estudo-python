pesos = []

for _ in range(5):
    peso = float(input('Digite o peso (em kg): '))
    pesos.append(peso)

maior = max(pesos)
menor = min(pesos)

print('O maior peso foi de {:.1f} kg e o menor de {:.1f} kg.'.format(maior, menor))
