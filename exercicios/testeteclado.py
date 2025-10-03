import random
palavra = ''
for c in range (0, 10):
    letra = chr(random.randint(97, 122))
    palavra = palavra +' '+ letra
print(palavra.upper())
palavra = palavra.replace(' ', '').upper()
palavra2 = input('Tente digitar essas letras : ').strip().upper()
if palavra == palavra2:
    for c in range(0, 100):
        print('Voce conseguiu !!!')
else:
    for c in range(0,100):
        print('O teclado esta falhando ou voce errou',c)
