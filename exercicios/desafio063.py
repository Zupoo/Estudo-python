n = int(input('Até qual numero da sequencia voce quer saber?'))
f1 = 1
f0 = 0
if n == 0:
    print('?')
elif n == 1:
    print(f0)
else:
    cont = 2
    print(f0)
    print(f1)
    while cont < n:
        fibo = f0 + f1
        print(fibo)
        f0 = f1
        f1 = fibo

        cont = cont+1