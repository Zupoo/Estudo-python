print('{:=^40}'.format('ZUPYSTORE'))
valor = float(input('Informe o preço do produto R$ : '))
x = int(input('''
Escolha a forma de pagamento :
[1] Para a vista no dinheiro ou cheque
[2] Para a vista no cartão
[3] Para em até 2x no cartão 
[4] Para 3x ou mais no cartão  
'''))

if x == 1:
    valor = valor * 0.9
    print('O novo preço do produto vai ser {}'.format(valor))
elif x == 2:
    valor = valor * 0.95
    print('O novo prelo do produto vai ser {}'.format(valor))
elif x == 3:
    print('Não tem alteração no preço do produto , ele continua por {:.2f}R$'.format(valor))
elif x ==4:
    parcela = int(input('Quantas parcelas? : '))
    if parcela < 3:
        print('Se voce deseja pagar em menos de 3x no cartão voce escolheu a opção errada')
    else:
        valor = valor * 1.20
        valorparcela = valor / parcela
        print('O valor de {} parcelado em {} parcelas de {:.2f} R$'.format(valor, parcela, valorparcela ))
else:
    print('A forma de pagamento selecionada é invalida')