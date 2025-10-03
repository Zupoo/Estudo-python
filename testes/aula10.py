nome = input('Qual o seu nome? : ')
if nome.strip().upper() == 'GUILHERME':
    print('Que nome lindo')
print('nome feio')


nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1+nota2) /2
if media >= 6:
    print('Parabens voce foi aprovado !!!')
else:
    print('Recuperação!!!')