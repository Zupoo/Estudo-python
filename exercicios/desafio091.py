import random
import time
armazem = {}
jogadores = []
maior = 0
menor = 0
# for c in range (0,4):
#     armazem['nome'] = input(f'Digite o nome do jogador {c} : ')
#     armazem['numerosorteado'] = random.randint(0,6)
#     jogadores.append(armazem.copy())
# print(jogadores)
# # x = sorted(jogadores['numerosorteado'])
# # print(x)
# for i in jogadores:
#     pri(i['numerosorteado'])

for c in range (0, 5):
    print(f'O len de jogadores é {len(jogadores)}')
    armazem['jogador'] = c
    armazem['dado'] = random.randint(0,6)
    print(f'O jogador {c} tirou {armazem['dado']}')
    # time.sleep(1)
    if c == 0:
        maior = armazem['dado']
        menor = armazem['dado']
    if armazem['dado'] >= maior:
        maior = armazem['dado']
        jogadores.insert(0, armazem.copy())
        print('adicionou no if aqui em cima em primeiro da lista')
        print(jogadores)


    else:
        for c in range(len(jogadores),0, -1):
            print(c)
            if armazem['dado'] <= (jogadores[c-1]['dado']):
                jogadores.insert(c, armazem.copy())
                break
    # else:
    #     for c, jogador in enumerate(jogadores):
    #         print(c,'aquio o C ')
    #         if armazem['dado'] >= jogador['dado']:
    #             jogadores.insert(c, armazem.copy())
    #             print('adicionou no else aqui em baixo como ', c, 'da lista')
    #             print(jogadores)

    #             break

print('-='*29)
for c, colocaçao in enumerate(jogadores):
    # time.sleep(1)
    print(f'{c+1}o lugar: Jogador {colocaçao['jogador']} com {colocaçao['dado']}')
