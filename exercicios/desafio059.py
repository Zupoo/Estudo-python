import time
n1 = int(input('Digite um numero : '))
n2 = int(input('Digite outro numero : '))
fazer = 0
resultado = 0
while fazer != 5:
    time.sleep(1)
    print(
    '''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    fazer = int(input(' Escolha uma opção : '))
    print('''
            ''')
    if fazer == 1:
        resultado = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, resultado))
    elif fazer == 2:
        resultado = n1 * n2
        print('{} x {} = {}'.format(n1, n2, resultado))
    elif fazer == 3:
        if n1 > n2:
            print('{} é o maior'.format(n1))
        elif n2 > n1:
            print('{} é o maior'.format(n2))
        else:
            print('São iguais')
    elif fazer == 4:
        n3 = n1
        n4 = n2
        n1 = int(input('Digite um novo numero'))
        n2 = int(input('Digite outro novo numero'))
        print('Voce acabou de alterar os numeros antes eram {} e {} agora são {} e {}'.format(n3, n4, n1, n2))
    elif fazer == 5:
        print('OK')
    else:
        print('Opção errada , tenten novamente')
    print( '--'*20)