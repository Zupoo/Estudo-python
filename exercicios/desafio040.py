nota1 = float(input('Digite a nota 1 : '))
nota2 = float(input('Digite a nota 2 : '))

media = (nota1 + nota2) / 2
print(media)
if media < 5:
    print('O aluno foi REPROVADO')
elif media >=5 and media <= 6.9:
    print('O aluno esta em RECUPERAÇÃO')
else:
    print('O aluno esta APROVADO')