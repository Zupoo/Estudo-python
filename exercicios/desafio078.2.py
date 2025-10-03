lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor : ')))
    print(lista)
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} na posição ', end='')
for c in range(0, len(lista)):
    if maior == lista[c]:
        print(c,'...', end = ' ')
print('')
print(f'O menor numero digitado foi {menor} e esta na posição ', end = '')
for c in range(0 , len(lista)):
    if menor == lista[c]:
        print(c,'...', end = ' ')