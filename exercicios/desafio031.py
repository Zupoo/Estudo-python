distancia = int(input('Digite qual a distancia da viagem em km : '))
if distancia <= 200:
    preço = distancia*0.5
    print('O preço da passagem é de {:.2f} R$'.format(preço))
else:
    preço = distancia*0.45
    print('O preço da passagem é de {:.2f} R$'. format(preço))

