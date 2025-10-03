'''
Analise
len(frase)  diz quantas letras tem
frase.count('o',0,13) conta quantas vezes tem a letra o
frase.find('deo') encontrar e diz aonde inicia oq estou procurando
'curso' in frase  só retorna se tem ou n

Transformação
frase.replace('Python', 'Android')
frase.upper()  metodo
frase.lower()
frase.capitalize()    1 letra maiouscola
frase.title()     1 letra de cada palavra maiuscola
frase.strip()     remove espaços inuteis
frase.rstrip()      strip da direita (r)
frase.lstrip        strip na esquerda


divisão
frase.split()      divide nos espaços e gera 1 lista com as palavras

junção
'-'.join(frase)




'''

frase = 'Curso em video'
dividido = frase.split()
print(dividido, len(frase), len(dividido[0]))
print(dividido[0][0], dividido[1][0], dividido[2][0])
frase2 = frase.replace('video', 'fembendazol')
print(frase, frase2)
print(frase2.count('e'))
print('curso' in frase2)
print(frase2.split())
print(frase2[2])
frase2 = frase2.split()
print(frase2[2])