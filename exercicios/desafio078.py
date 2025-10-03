lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor')))
print(lista)
maior = max(lista)
print(f'O maior numero digitado foi {maior} e ele esta nas posiçoes {lista.index(maior)+1}', end = '')
for c in range(lista.index(maior)+1, len(lista)):
    if lista[c] == maior:
        print(' e',c + 1)

print('')
print('---'*20)

menor = min(lista)
localmenor = lista.index(menor)
print(f'menor encontrado foi o {menor} e esta na posição {localmenor+1}' ,end = '')
for i in range(localmenor+1 ,len(lista)):
    if lista[i] == menor:
        print(' e',i+1, end = '')