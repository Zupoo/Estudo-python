nome = input('Digite seu nome : ')
sexo = input('Digite o sexo [M] para masculino ou [F] para feminino : ').upper()
#quando essa afirmação torna falsa eu paro
while sexo != 'M' and sexo != 'F': # enquanto sexo for diferente de 'M' e diferente de 'F'.quando essa afirmação torna falsa eu paro
    print('Voce digitou um caractere nao cadastrado , por favor tente novamente')
    sexo = input('Digite o sexo [M] para masculino ou [F] para feminino : ').upper()
print('Seu nome é {} e o sexo é {}'.format(nome, sexo))


# sexo = ' '
# while sexo not in 'MmFf' or sexo == '':
#     sexo = str(input('Sexo [M/F]: ')).strip().upper()
# print('Sexo {} registrado com sucesso.'.format(sexo)


#faça um if para saber se é M ou F
a = -1
while a != 0: #só sai quando essa afirmação torna falsa eu paro
    if sexo != 'M' or sexo != 'F':
        print('Digitou errado dog')
        sexo = input('Digite o sexo [M] para masculino ou [F] para feminino : ').upper()
    else:
        a = 0
        print('legal dog')
