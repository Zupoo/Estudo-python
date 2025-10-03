cidade = input('Em qual cidade voce mora? :').strip()
cidade2 = cidade
cidade = cidade.upper().split()
print(cidade)
print(cidade[0] == 'SANTO')
print('A cidade escolhida {} começa com santo '.format('SANTO' in cidade[0]))


print(cidade2[:5]== 'SANTO')

