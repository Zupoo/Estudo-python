dicionario = {}
golsp = []
soma = 0
dicionario['nome'] = input('Nome do jogador : ')
partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou?'))
for c in range (0,partidas):
    golsp.append(int(input(f'Quantos gols o {dicionario['nome']} fez na partida {c+1} :')))
dicionario['gols'] = golsp[:]
dicionario['total'] = 0
for i in dicionario['gols']:
    print(i)
    soma = soma + i
dicionario['total'] = soma
print('-='*20)
for v,k in dicionario.items():
    print(f'O campo {v} tem o valor {k}')
print('-='*20)
print(f'O jogador {dicionario['nome']} jogou {partidas} partidas')
for partida , gols in enumerate(dicionario['gols']):
    print(f'Na partida {partida+1} {dicionario['nome']} fez {gols} gols')
print('-='*20)
for c in range(0,len(dicionario['gols'])):
    print(f'Na partida {c} o {dicionario["nome"]} fez {dicionario["gols"][c]} gols')
print(f'Foi um total de {dicionario['total']} gols nas {partidas} partidas')
print('-='*20)
print(dicionario)

print(f'len de jogador {len(dicionario['gols'])} / partidas {partidas}')