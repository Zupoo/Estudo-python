base = float(input('Qual informe uma das medidas da parede'))
h = float(input('Informe a outra medida da parede'))
a = base*h
tinta = a/2
print('Vai ser usado {} litros de tinta para pintar uma parede com a area de {} metros quadrados'.format(tinta, a))