total = 0
maisdemil = 0
preçobarato = 0
nomebarato = ''
while True:
    nome = input('Informe o nome do produto')
    preço = float(input('Informe o preço do produto'))
    while True:
        continuar = input('Voce deseja registrar mais produtos? [S/N] : ').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
    total = total + preço
    if preço > 1000:
        maisdemil = maisdemil + 1
    if nomebarato == '' and preçobarato == 0 or preço < preçobarato:
        nomebarato = nome
        preçobarato = preço
    # elif preço < preçobarato:
    #     preçobarato = preço
        nomebarato = nome
    elif preço == preçobarato:
        nomebarato = nomebarato +', ' + nome
    if continuar == 'N':
        break
print(f'O total gasto na compra foi de R$ {total:.2f} e {maisdemil} produtos tiveram o valor de mais de 1.000 R$')
print(f'O nome do produto mais barato é {nomebarato} e custou {preçobarato:.2f} R$')

