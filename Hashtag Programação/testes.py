import numpy as np

rng = np.random.default_rng()
print(rng)

numero = rng.random() *100
print(numero)

array_aleatorio = rng.random(5) *10
print(array_aleatorio)


rng = np.random.default_rng(seed= 0)
numeros = rng.integers(low= 51, high= 200, size= 31)
print(numeros)

lista = list(numeros)
teste = lista.index(96)
print(teste)

noventaeceis = np.where(numeros == 96)
print(noventaeceis)
print(numeros[noventaeceis])

print(np.where((numeros > 95) & (numeros < 97), numeros * 9999, numeros))
print('=*'*20)
print(np.where((numeros == 96), numeros * 10, numeros))







importar
armazenar um arquivo csv
printar ele
mudar nome 
display()
escolher só a coluna que quer
mostrar só algumas linhas 0: -1:
fazer merge


counts() conta quantas vezes aparece
.ploy() criar grafico
groupby()junta e soma tudo q se repete
