tupla = ("maca", "banana" ,"carro", "livro", "cachorro", "flor", "sol", "lua", "gato", "amigo", "felicidade", "coracao")
qtdpalavras = (len(tupla))
vogais = ('a', 'e', 'i', 'o', 'u')
print(qtdpalavras,'qtd palabras')
# for c in range(0,qtdpalavras): #fazer o for a quantidade de vezes q tem de palavras na tupla
#     print(f'Palavra da vez {tupla[c]} ')
#     for i in range (0, len(tupla[c])): # fazer o for a quantidade de vezes q tem de letras na palavra
#         if tupla[c][i].upper() == 'A':
#             print(tupla[c][i],' ', end = '')
#     for i in range (0,len(tupla[c])):
#         if tupla[c][i].upper() == 'E':
#             print(tupla[c][i],' ', end = '')
#     for i in range (0,len(tupla[c])):
#         if tupla[c][i].upper() == 'I':
#             print(tupla[c][i],' ', end = '')
#     for i in range (0,len(tupla[c])):
#         if tupla[c][i].upper() == 'O':
#             print(tupla[c][i],' ', end = '')
#     for i in range (0,len(tupla[c])):
#         if tupla[c][i].upper() == 'U':
#             print(tupla[c][i],' ', end = '')
#     print('')

for c in range(0,qtdpalavras): #fazer o for a quantidade de vezes q tem de palavras na tupla
    print(f'Palavra da vez {tupla[c]} ', end = '')
    for i in range (0, len(tupla[c])): # fazer o for a quantidade de vezes q tem de letras na palavra
        if tupla[c][i] in vogais:
            print(tupla[c][i], end = '')
    print('')
