import random
print('-='*15)
print('Vamos jogar par ou impar')
print('-='*15)
vitorias = 0
while True:
    npc = random.randint(0,10)
    print('Já pensei em um numero.', npc)
    n = int(input('Qual numero voce quer ? : '))
    pi = 0
    while pi != 'P' and pi != 'I':
        pi = input('Voce quer par ou impar? [Digite P ou I]').strip().upper()[0]
    soma = npc + n
    if soma % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'
    if resultado == 'par' and pi == 'P':
        print(f'Voce ganhou , o computador escolheu {npc} e {n}+{npc}={soma} e {soma} é par')
        vitorias = vitorias + 1
    elif resultado == 'impar' and pi == 'I':
        print(f'Voce ganhou , o computador escolheu {npc} e {n}+{npc}={soma} e {soma} é impar')
        vitorias = vitorias + 1
    else:
        break
print('GAME OVER ')
if resultado == 'par' and pi != 'P':
    print(f'Voce perdeu , o computador pensou em {npc} e deu PAR')
    print(f'Voce venceu {vitorias} vezes do computador')
else:
    print(f'Voce perdeu , o computador pensou em {npc} e deu IMPAR')
    print(f'Voce venceu {vitorias} vezes do computador')
