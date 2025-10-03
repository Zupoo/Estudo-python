import random
aluno1 = input('Digite o nome de um aluno')
aluno2= input('Digite o nome de outro aluno')
aluno3 = input('Digite o nome de outro aluno')
aluno4 = input('Digite o nome de outro aluno')

a = random.sample([1 , 2 , 3, 4], k=4)
print('A ordem a ser apresentada vai ser : {}'.format(a))
print('Aluno 1 = {}\nAluno 2 = {}\nAluno 3 = {}\nAluno 4 = {}'.format(aluno1, aluno2, aluno3, aluno4))