#Adicionar,Modificar e remover itens do Dicionário
aquario_animais = {'peixes': ['palhaço macho', 'palhaço femea'],'corais': ['torch', 'hammer'], 'anemonas': ['Bbt rainbow', 'Bbt redfire']}

aquario_equipamentos = {'bombas': ['sicce 1.5', 'MJ GF 308'], 'luminaria': 'MJ-L260', 'skimmer': 'AquaExel 70D'}

print('Adicionando algo a um dicionario')
dicionario_vazio = {}
dicionario_vazio['chave'] = 'olá'
dicionario_vazio['chave2'] = 'olá2'
print(dicionario_vazio)

print('---'*20)
print('modificando um dicionario')
dicionario_vazio['chave2'] = 'Bom dia!'
print(dicionario_vazio)

print('---'*20)
print('removendo algo do dicionario com o del')
del dicionario_vazio['chave2']
print(dicionario_vazio)

dicionario_vazio['chave2'] = 'oie'

print('---'*20)
print('removendo algo do dicionario e armazenando em uma variavel o valor com o pop')
armazenar = dicionario_vazio.pop('chave2')
print(dicionario_vazio)
print(armazenar)

print('---'*20)
print('Limpando o dicionario com o .clear()')
print(dicionario_vazio)

dicionario_vazio.clear()
print(dicionario_vazio)

print('---'*20)
#adcionando algo a um dicionario com update
dicionario_vazio2 = {}
dicionario_vazio2.update({'chave': 'valor'})
print(dicionario_vazio2)

#juntando 2 dicionarios
aquario_animais.update(aquario_equipamentos)
print(aquario_animais)

