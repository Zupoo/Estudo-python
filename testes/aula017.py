num = [2, 5, 9, 1]
num[2] = 3
num.append(7) # adiciona na listas como ultimo
num.sort(reverse= True)   # .sort coloca em ordem .sort(reverse = True) coloca na ordem ao contrario
num.insert(2, 111)  #adiciona o 00 na posição 2 da lista 
num.pop() # elimina o ultimo da lista
num.pop(0) #elimina o numero na posição q eu escolher
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.remove(111) #remove quem um escolher indepenente da posição (elimina o primeiro q encontrar por exemplo)
print(num)
num.append(99)
num.append(99)
num.append(99)
print(num)
num.remove(99) #só removeu o primeiro 99 se n encontrar vai dar erro
print(num)

valores = []
for cont in range (0, 5):
    n = int(input('Digite um numero para inserir na lista : '))
    valores.append(n)
    print(valores)
for c, v in enumerate(valores):
    print(f' Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')

for c in range(0, len(valores)):
    print(f'Na posição {c} encontrei o valor {valores[c]}')
print('Tb cheguei ao final da lista')

a = [1, 2, 3, 4, 5]
b = a
print(b)
print(a)
b[1] = 999  #como eu disse q b = a qualquer alteração feita em B vai ser feita em A , para isso n acontecer tem q colocar [:]
a[2] = 888
print(b, a)
c = a[:]  #dessa forma eu digo q C é uma copia de A entao a alteração nao vai ser feita nos 2
print(c)
c[2] = 5
print(c , a)