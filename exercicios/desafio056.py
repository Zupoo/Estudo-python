somaidade = 0
nomemaisvelho = ''
idademaisvelho = 0
fmenos20 = 0
for c in range(0 , 4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite M ou F para o sexo').upper().strip()
    somaidade = somaidade + idade #somando as idades para calcular a media
    if sexo == 'M' and idade > idademaisvelho: #verificando se é homem e se a é o mais velho
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        fmenos20 = fmenos20+1


media = somaidade/4
print('Media de idade do grupo é {} anos'.format(media))
if nomemaisvelho !='' or idademaisvelho != 0:
    print('O homem mais velho é o {} com {} anos'.format(nomemaisvelho, idademaisvelho))
print('Tem {} mulheres com menos de 20 anos no grupo'.format(fmenos20))