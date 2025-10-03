cont1 = fechado = cont2 = 0
lista = []
lista.append(input('Digite uma expressão apenas com parenteses : '))
print('-.-.'*30)
while True:
    for c in range(0, len(lista[0])):
        if lista[0][c] == '(':
            cont1 = cont1 + 1
            fechado = fechado + 1
        if lista[0][c] == ')':
            cont2 = cont2 + 1
            fechado = fechado - 1
            if fechado < 0 :
                break
    break
if cont1 == cont2:
     print(f'Essa expresão é valida')
else:
     print(f'Essa expressão não é valida')