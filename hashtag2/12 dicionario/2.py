#Pegar item Dicionario e verificar item Dicionário
aquario_animais = {'peixes': ['palhaço macho', 'palhaço femea'], 'corais': ['torch', 'hammer'], 'anemonas': ['Bbt rainbow', 'Bbt redfire']}

aquario_equipamentos = {'bombas': ['sicce 1.5', 'MJ GF 308'], 'luminaria': 'MJ-L260', 'skimmer': 'AquaExel 70D'}


print(f"Os corais desse aquario são {aquario_animais['corais']}")
print(f"Os peixes desse aquario são {aquario_animais.get('peixes')}")


consulta_equipamento = input('Sobre qual equipamento do aquario voce quer saber?')
if consulta_equipamento in aquario_equipamentos:
    print(f"A/as {consulta_equipamento} utilizada no aquario : {aquario_equipamentos[consulta_equipamento]}")
else:
    print('não tem')


consulta_equipamento = input('Sobre qual equipamento do aquario voce quer saber?')
verificar = aquario_equipamentos.get(consulta_equipamento)
print(verificar)


