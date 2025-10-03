dicionario = {}
lista = []
somaidade = 0
while True:
    continuar = ''
    dicionario['nome'] = input('Nome : ')
    while True:  
        dicionario['sexo'] = input('Sexo [F/M] : ').upper().strip()
        if dicionario['sexo'] in 'MF':
            break
        else:
            print(f'Erro , por favor digite apenas M ou F')
    dicionario['idade']= int(input('Idade : '))
    lista.append(dicionario.copy())
    dicionario.clear()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Quer cadastrar mais pessoas?[S/N] : ').strip().upper()
    if continuar == 'N':
        break
print(lista)
print(f'Foram cadastradas {len(lista)} pessoas')
for c in lista:
    somaidade = somaidade + c['idade']
print(f'A média de idade do grupo é de {somaidade / len(lista)} anos')
print('Lista das mulheres', end = '')
for c in lista:
    if c['sexo'] == 'F':
        print(f' {c['nome']}', end = '')
print('')
print('Lista das pessoas q estou com a idade acima da media do grupo ')
for c in lista:
    if c['idade'] > somaidade/len(lista):
        print('')
        for v , k in c.items():
            print(f'{v} = {k}   ' , end = '')


