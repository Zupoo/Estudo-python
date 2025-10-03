import random
import time
import operator
dados = {'jogador1' : random.randint(0,6) , 'jogador2' : random.randint(0,6) , 'jogador3' : random.randint(0,6) , 'jogador4' : random.randint(0,6)
}
print(dados)
for k, v in dados.items():
    print(f'O {k} tirou {v} no dado')
ranking = {}
ranking = sorted(dados.items(), key = operator.itemgetter(1), reverse= True)
print(ranking)
print('-='*33)
print('== TANKING DOS JOGADORES ==')
for c, v in enumerate(ranking):
    print(f'{c+1}º lugar: {v[0]} que sorteou o nuemro {v[1]}') 
    time.sleep(0.5)