frase = input('Digite uma frase para verificar se ela é um PALINDROMO : ')
frase = frase.strip().replace(' ', '').upper()
letras = len(frase)
print(letras)
frase2 = ''
for c in range(letras-1, 0 -1, -1):
    frase2 = frase2 + frase[c]

if frase == frase2:
    print('A frase é um PALINDROMO')
else:
    print('A frase não é um palindromo porque {} não é igual a {}'.format(frase , frase2))

