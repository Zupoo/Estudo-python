import math
ang = int(input('Digite um angulo qualquer: '))
angrad = math.radians(ang)
sen = math.sin(angrad)
cos = math.cos(angrad)
tg = math.tan(angrad)
print('O seno de {:.2f} é {:.2f} e o cosseno é {:.2f}'.format(ang, sen, cos))
print(tg,'tangente')
