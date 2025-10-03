
n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
rd = n1%n2
e = n1**n2

print('A soma é {} \n a multiplicação é {} a divisão é {:.2f} a divisão interira é {}'.format(s, m, d, di), end=' ')
print('O resto da divisão é {} a potencia é {}'.format(rd, e))

