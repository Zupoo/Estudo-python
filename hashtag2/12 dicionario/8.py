# transformar listas em dicionario

lista_extenso = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis']

lista_algarismos = [1, 2, 3, 4, 5, 6]

lista_tupla = [('um', 1), ('dois', 2), ('tres', 3), ('quatro', 4), ('cinco', 5)]

# forma 1 , criar o dicionario a partir de uma lista e os valores das chaves padrao/zerado

dicionario = dict.fromkeys(lista_extenso, 0)
print(dicionario)
print('-'*55)
# forma 2, criar um dicionario se voce tiver uma lista de tuplas
dicionario_tuplas = dict(lista_tupla)
print(dicionario_tuplas)
print('-'*55)
#forma 3, criar um dicionario tendo 2 listas
lista_junta = zip(lista_extenso, lista_algarismos)
dicionario2 = dict(lista_junta)
print(dicionario2)

