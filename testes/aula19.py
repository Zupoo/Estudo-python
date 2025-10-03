# pessoa1 = {'nome' : 'Guilherme' , 'sexo': 'M', 'idade' : 24}
# pessoa2 = {'nome': 'Nanci', 'sexo' : 'F' , 'idade' : 58}
# print(f'O {pessoa1["nome"]} tem {pessoa1["idade"]} anos')
# print(pessoa1.keys())
# print(pessoa1.values())
# print(pessoa1.items())
# print('-'*39)
# for k in pessoa1.keys():
#     print(k)
# print('-'*39)
# for k in pessoa1.values():
#     print(k)
# print('-'*39)
# for c , i in pessoa1.items():
#     print(f'{c} = {i}')
# del pessoa1['sexo']
# pessoa1['nome'] = 'Zupo'
# print('-'*39)
# pessoa1['peso'] = 120
# pessoa1 = {'nome' : 'Guilherme' , 'sexo': 'M', 'idade' : 24}
# for c , i in pessoa1.items():
#     print(f'{c} = {i}')
# for n , z in pessoa2.items():
#     print(f'{n} = {z}')
# pessoas = []
# pessoas.append(pessoa1)
# pessoas.append(pessoa2)
# print(pessoas)
# print(pessoas[0]['nome'])
# print(pessoas[1]['nome'])

pessoa1 = {}
pessoas = []
for c in range (0,3):
    pessoa1['nome'] = input('Digite o nome : ')
    pessoa1['idade'] = int(input('Digite a idade'))
    pessoas.append(pessoa1.copy())
print(pessoas)
for p in pessoas:
    print(p)
    for k, v in p.items():
        print(k ,v)

for c in range(0,len(pessoas)):
    print(pessoas[c])
    for k , v in pessoas[c].items():
        print(k,v)
