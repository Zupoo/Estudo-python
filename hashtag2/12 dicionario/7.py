aquario_animais = {'peixes': ['palhaço macho', 'palhaço femea'],'corais': ['torch', 'hammer'], 'anemonas': ['Bbt rainbow', 'Bbt redfire']}

aquario_equipamentos = {'bombas': ['sicce 1.5', 'MJ GF 308'], 'luminaria': 'MJ-L260', 'skimmer': 'AquaExel 70D'}

aquario_completo = {}

# testando juntar 2 listas sem alterar elas
aquario_completo.update(aquario_animais)
aquario_completo.update(aquario_equipamentos)

print(aquario_completo)

print(aquario_animais.keys())
print(aquario_animais.values())

print(list(aquario_animais.keys()))
print(list(aquario_animais.values()))

#colocando a lista completa em com as chaves em ordem alfabetica
print('--'*50)
chaves_aquario_completo = aquario_completo.keys()
# agora precisa transfor em lista
chaves_aquario_completo = list(chaves_aquario_completo)
# agora sim pode usar o .sort
chaves_aquario_completo.sort()
print(chaves_aquario_completo)
for chave in chaves_aquario_completo:
    print(chave, aquario_completo[chave])