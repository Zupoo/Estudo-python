produtos = ['tv', 'celular', 'mouse']
print(produtos[1:])

## pra descobrir aonde esta o item em uma lista se usa o index
# se nao encontrar oq esta procurando da erro entao pode se usar o in pra verificar se tem antes
if 'celula' in produtos:
    i = produtos.index('celula')
    print('posição' ,i, produtos[i])
else:
    print('tem celula não , escreve direito')

#adicionar item no final lista
# Adicionar:<br>
# lista.append(item)

# Remover:<br>
# item_removido = lista.pop(indice)<br>
# lista.remove(item)
produtos.append('ratazana')
produtos.append('xadrez')
produtos.append('cafe')
print(produtos)
produtos.remove('celular')
print(produtos)
item_removido = produtos.pop(0)
print(f'foi removido o item {item_removido} da lista {produtos}')

#try except
try:
    produtos.remove('xadrezex')
    print(f'xadrez removido da lista')
except:
    print('xadrezzz não foi encontrado na lista')
print(produtos)

## maior valor max() menor valor min()

## formas de somar listas
#não se deve adicionar uma lista a outra com apend , se nao fica uma lista dentro da outra
# lista.extend(lista2)
#lista_nova = lista1 + lista2

novos_produtos = ['margarina' , 'saco de bala', 'arroz', 'feijão' , 'cenoura']
total_produtos = produtos + novos_produtos
print(total_produtos)
produtos_limpeza = ['alvejante', 'sabão em pó', 'detergente']
total_produtos.extend(produtos_limpeza)
print(total_produtos)

#ordenar usar lista.sort()
lista = [5, 6, 2, 10, 9, 8]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
maior = max(lista)
menor = min(lista)
print(maior , menor)

#mostrando a lista mais bonita e transformando ela em uma string
print('\n'.join(total_produtos))
deslistar = '/'.join(total_produtos)
print(deslistar)
print(deslistar[0])

#transformando uma string com varias coisas em uma lista
futura_lista = 'sofa, cadeira, mesa, televisão. guarda roupas, chinelo, abelha'
atual_lista = futura_lista.split(', ')
print(atual_lista)
atual_lista.pop(0)
print(atual_lista)


## cuidado ao fazer atribuiçoes com listas pq se vc disse lista2 = lista qualuqer alteraçao em uma delas a outra vai sofre tb
#para copiar listas temos q usar .copy ou lista2 = lista[:]
#caso tenha listas dentro de lista deve ser usado a biblioteca copy.deepcopy(lista)
listax = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listay = listax
listaz = listax.copy()
listay[0] = 11
listaz[0] = 9999999
print(listax , listay, listaz)




