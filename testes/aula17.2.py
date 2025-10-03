galera = [['João', 19], ['Angelica', 33], ['Samanta', 24], ['Rafaela', 19]]
for c in galera:
    print(c[0])

for c in range(0, 4):
    print(galera[c][0])


lista = []
aux = []

for c in range (0, 3):
    aux.append(input('Digite o nome: '))
    aux.append(int(input('Digite a idade: ')))
    lista.append(aux[:])
    aux.clear()
print(lista)
