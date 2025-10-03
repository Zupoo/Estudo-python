km = float(input('Digite a quantidade de km percorridos: '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preco = (dias*60) + (0.15*km)
print('O valor pelo carro q percorreu {}km e foi alugado por {} dias é de {:.2f} R$.'.format(km, dias, preco))