aquario_animais = {'peixes': ['palhaço macho', 'palhaço femea'],'corais': ['torch', 'hammer'], 'anemonas': ['Bbt rainbow', 'Bbt redfire']}

aquario_equipamentos = {'bombas': ['sicce 1.5', 'MJ GF 308'], 'luminaria': 'MJ-L260', 'skimmer': 'AquaExel 70D'}

aquario_completo = {}

# testando juntar 2 listas sem alterar elas
aquario_completo.update(aquario_animais)
aquario_completo.update(aquario_equipamentos)

print(aquario_animais.items())


# percorrendo o dicionario usando o for
for itens in aquario_completo.items():
    print(itens)

print('-'*50)

# percorrendo o dicionario e fazendo o unpecked
for chave, valor in aquario_completo.items():
    print(f'{chave} {valor}')
    
print('-'*50)

# fazendo a mesma coisa que o de cima só que sem usar o .items()
for chave in aquario_completo:
    valor = aquario_completo[chave]
    print(f'{chave} {valor}')
        

print('-'*50)
print('-'*50)

