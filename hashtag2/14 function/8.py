# função com valor padrao é só na hora de definir a função colocar o = e o valor padrao q voce quer
# ai se nao passar nada vai usar o padrao, caso queira mudar é só escrever o nome do parametro e atribuir um valor pra ele
def padronizar(lista, padrao = 'm'):
    lista_padronizada = []
    if padrao == 'M':
        for item in lista:
            item = item.upper().strip()
            lista_padronizada.append(item)
        
    elif padrao == 'm':
        for item in lista:
            item = item.lower().strip()
            lista_padronizada.append(item)  
    return lista_padronizada        
    
print(padronizar(['Aaa', 'BbbB', 'CcCcCCc'], padrao = 'M'))

