cont = 0
while True:
    n = int(input('Voce quer saber a tabuada de qual numero? (se quiser parar digite um numero negativo)'))
    print('-'*20)
    if n < 0:
        break
    for c in range(0,11):
        resultado = n * c
        print(f'{n} x {c} = {resultado}')
    print('-'*20)
print('FIM')

