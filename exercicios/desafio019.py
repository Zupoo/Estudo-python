#dificil
import random
aluno1 = input('Digite o nome do aluno 1')
aluno2 = input('Digite o nome do aluno 2')
aluno3 = input('Digite o nome do aluno 3')
aluno4 = input('Digite o nome do aluno 4')

sorte = random.randint(1, 4)

print('O aluno sorteado a apagar o aquario foi a aluno {}'.format(sorte))
print('Aluno 1 -> {}\nAluno 2 -> {}\nAluno 3 -> {} \nAluno 4 -> {}'.format(aluno1, aluno2, aluno3, aluno4))
