frase = input('Digite uma frase: ')
print('Aparecem {} a letra A na frase'.format(frase.upper().count('A')))

print('A letra A aparece pela primeira vez na posição {} da frase'.format(frase.upper().strip().find('A')+1))

print('A letra A aparece pela ultima vez na posição {} da frase'.format(frase.upper().strip().rfind('A')+1))