def escreva(n):
    for c in range(0, len(n)):
        caractere = len(n[c])
        print('~'*caractere)
        print(n[c])
        print('~'*caractere)
    print('')

destaque = []
destaque.append(input('O que voce quer q seja escrito em destaque ? '))
while True:
    continuar = input('Quer escrever mais alguma coisa?[S/N] : ').strip().upper()
    if continuar in 'NS':
        if continuar == 'N':
            break
        else:
            destaque.append(input('O que mais voce quer q seja escrito em destaque? : '))
escreva(destaque)

def izi(izi):
    letras = len(izi)
    print('~'*letras)
    print(izi)
    print('~'*letras)


izi('Olá Mundo!')