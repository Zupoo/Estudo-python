nota50 = nota20 = nota10 = nota1 = 0
while True:
    saque = int(input('Quanto voce deseja sacar?'))
    print(saque)
    while saque >= 50:
        saque = saque - 50
        nota50 = nota50 + 1
        print(saque,'50')
    while saque >= 20:
        saque = saque - 20
        nota20 = nota20 + 1
        print(saque,'20')
    while saque >= 10:
        saque = saque - 10
        nota10 = nota10 + 1
        print(saque,'10')
    while saque >= 1:
        saque = saque - 1
        nota1 = nota1 + 1
        print(saque,'1')
    if saque == 0:
        break
print('''
            Total de cédulas
      
{} cedulas de 50 reais
{} cédulas de 20 reais
{} cédulas de 10 reais
{} cédulas de 1 real
      '''.format(nota50, nota20, nota10, nota1))