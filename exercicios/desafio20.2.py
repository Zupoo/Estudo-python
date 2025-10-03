import random
aluno1 = input('Digite o nome de um aluno')
aluno2= input('Digite o nome de outro aluno')
aluno3 = input('Digite o nome de outro aluno')
aluno4 = input('Digite o nome de outro aluno')


ordem = random.sample([aluno1, aluno2, aluno3, aluno4], k=4)
print(ordem)