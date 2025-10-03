soma = 0
for c in range(0, 6):
    n = int(input('Digite algum numero'))
    if n % 2 == 0:
        soma = soma + n
print('A soma apenas dos numeros pares digitados é : ',soma)