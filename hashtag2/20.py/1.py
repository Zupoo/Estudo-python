#funcao map
#ela aplica uma funcao para cada item do iterable

def soma(n, indice):
    n += indice
    return n

lista = [1, 2, 3, 4, 5]
indice = 1

lista_somada = list(map(soma, lista, indice))
print(lista_somada)