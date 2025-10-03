lanche = ('Hambúrguer' , 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[0])
print(lanche[1:4])
print(lanche[-1])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[:-2])
#tuplas sao imutaveis
print('-='*20)
for c in lanche:
    print(c)
print('-='*20)

cont =0
for c in range (0 , len(lanche)):       #gostei mais desse
    print(lanche[c], c)
print('-='*20)

for c in lanche:
    cont = cont + 1
    print(c, cont)
print('-='*20)

for pos, c in enumerate(lanche):
    print(c, pos)
    print()

print(sorted(lanche))

lanche = (sorted(lanche))
print(lanche)

a= (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8)) #procura em qual posição da tupla esta o q vc colocar entre parenteses
print(c[4])
print(c[0:5])
print(c)
print(c.index(5))
print(c.index(5,2)) #procura apartir do numero depois da , 
print('-='*50)