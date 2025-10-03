armazem = {}
armazem['nome'] = input('Nome: ')
armazem['nota'] = float(input(f'Média de {armazem['nome']} : '))
print(f'Nome é igual a {armazem['nome']}')
print(f'Média é igual a {armazem['nota']}')
if armazem['nota'] >= 7:
    armazem['situação'] = 'aprovado'
elif armazem['nota'] >= 5 and armazem['nota'] < 7:
    armazem['situação'] = 'recuperação'
else:
    armazem['situação'] = 'reprovado'
print(f'Situação é igual a {armazem['situação']}')