# passar quantidade indefinida de parametros pra função
# é só colocar o * antes do nome do parametro na hora de criar a função
# com isso o parametro vira uma tupla 

def soma(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma

print(soma(1,2,34,5,6,62,3,2))    

# se quiser passar com keyword só colocar dois **
# e ele vai como dicionario
# copiei o codigo da aula pq n consegui pensar em nada pra usar isso como exemplo
# o **adicionais vem como dicionario
def preco_final(preco, **adicionais):
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garatia_extra' in adicionais:
        preco += adicionais['garantia_extra']     
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco        