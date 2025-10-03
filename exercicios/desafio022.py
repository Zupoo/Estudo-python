nome = input('Digite o nome completo: ').strip()

print('Nome em maiuscolo {}'.format(nome.upper()))

print('Nome em minusculo {}'.format(nome.lower()))

espaços = nome.count(' ')
print('O nome completo tem {} letras sem considerar espaços'.format(len(nome) - espaços))

div = nome.split()
print(div)
print('O Primeiro nome tem {} letras'.format(len(div[0])))
