import datetime
nasc = int(input('Informe a data de nascimento do atleta : '))

ano = anoatual = datetime.date.today().year
idade = ano - nasc
print(idade)

if idade <= 9:
    print('Atleta da categoria MIRIM')
elif idade <= 14:
    print('Atleta da categoria INFANTIL')
elif idade <= 19:
    print('Atleta da categoria JUNIOR')
elif idade <= 25:
    print('Atleta da categoria SÊNIOR')
else:
    print('Atleta da categoria MASTER')
