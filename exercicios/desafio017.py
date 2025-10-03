import random
import math
ca1 = random.randint(1,10)
ca2 = random.randint(1,10)
hipot = math.sqrt(ca1**2 + ca2**2)
print('{} é o valor de um cateto , {} é o valor de outro cateto e {:.2f} é o valor da hipotenusa'.format(ca1, ca2, hipot))

