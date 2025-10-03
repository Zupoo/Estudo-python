lista = []
dicionario = {}
while True:
    soma = 0
    dicionario['nome'] = input('Nome do jogador : ')
    partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou?'))
    golsp = []
    for c in range (0,partidas):
        golsp.append(int(input(f'Quantos gols o {dicionario['nome']} fez na partida {c+1} :')))
    dicionario['gols'] = golsp.copy()
    dicionario['total'] = 0
    for i in dicionario['gols']:
        soma = soma + i
    dicionario['total'] = soma
    print('-='*20)
    lista.append(dicionario.copy())
    dicionario.clear()
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = input('Quer continuar [S/N] : ').strip().upper()
    if continuar == 'N':
        break
print('-='*33)
print(lista)
print('-='*33)
a = ''
print(f'Codigo{a:.<10} Nome{a:.<10} Gols{a:.<10} Total{a:.<10}')
for x, c in enumerate(lista):
    print(f'{x: <18}', end = '')
    for y in c.values():
        print(f'{y}{a: <14}', end = '')
    print('')
    # for v in c.values():
    #     print(f'{x:.<10}{v}{a:.<10}', end='')
# for c in range(0, len(lista)):
#     for v , k in items
while True:
    info = input(f'Se quiser mais informação sobre algum jogador?[S/N] :').strip().upper()
    if info == 'N':
        break
    elif info == 'S':
        cod = int(input('Informe o codigo do jogador : '))
        if cod >= len(lista):
            print('Codigo invalido')
        else:
            print(f'== Gols do jogador {lista[cod]['nome']} ==')
            for n, c in enumerate(lista[cod]['gols']):
                print(f'Na partida {n+1} fez {c} gols')
    else:
        print('Responda apenas com [S ou N]')


