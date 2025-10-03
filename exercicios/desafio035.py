r1 = int(input('Qual o tamanho do seguimento de reta 1 ?'))
r2 = int(input('Qual o tamanho do seguimento de reta 2 ?'))
r3 = int(input('Qual o tamanho do seguimento de reta 3 ?'))

cont = 0

if r1 + r2 > r3:
    cont = cont + 1
if r2 + r3 > r1:
    cont = cont + 1
if r1 + r3 > r2:
    cont = cont + 1

if cont == 3:
    print('Com esses seguimentos de reta é possivel se foramr um triangulo!')
else:
     print('É impossivel formar um triangulo com esses seguimentos de reta')

