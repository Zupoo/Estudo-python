import datetime
ano = datetime.date.today().year
demaior = 21
maioridade = 0
idade = 0
for c in range(0, 7):
    nasc = int(input('Qual o seu ano de nascimento? : '))
    idade = ano - nasc
    if idade >= demaior:
        maioridade = maioridade + 1
print(maioridade)
menoridade = 7 - maioridade
print(menoridade)