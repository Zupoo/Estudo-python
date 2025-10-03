import datetime
dicionario = {}
dicionario['nome'] = input('Nome : ')
dicionario['nasc'] = int(input('Ano de nascimento : '))
dicionario['carteira'] = int(input('Carteira de trabalho (caso nao tenha digite zero) : '))
anoatual= ano = datetime.date.today().year
dicionario['idade'] = anoatual - dicionario['nasc']
if dicionario['carteira'] != 0:
    dicionario['contratação'] = int(input('Informe o ano de contratação'))
    dicionario['salario'] = float(input('Informe o salário R$ : '))
    dicionario['anoaposentar'] = dicionario['contratação'] + 35
    dicionario['idadeaposentar'] = dicionario['anoaposentar'] - dicionario['nasc']
print('-='*33)
print(dicionario)
print(f'nome tem o valor {dicionario['nome']}')
print(f'idade tem o valor {dicionario['idade']}')
if dicionario['carteira'] != 0:
    print(f'ctps tem o valor {dicionario['carteira']}')
    print(f'contratação tem o valor {dicionario['contratação']}')
    print(f'salário tem o valor de R$ {dicionario['salario']:.2f}')
    print(f'aposentadoria tem o valor de {dicionario['idadeaposentar']}')
print('+++++++++++++'*10)
for v , k in dicionario.items():
    print(v,k)
