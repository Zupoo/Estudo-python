soma = 0
flag = 999
n=0
while n != flag:
    n = int(input('Digite quantos numeros quiser , caso queira parar digite 999 '))
    if n != 999:
        soma = soma + n
        print(soma)
print(f'A soma dos numeros digitados é {soma}')