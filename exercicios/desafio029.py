v = int(input('Qual a velociade do carro em km/h? : '))
if v >= 80:
    multa = (v - 80) * 7
    print('Voce foi multado e a multa vai custar {:.2f} R$'.format(multa))
else:
    print('Não foi multado {}km/h esta dentro da velocidade permitida'.format(v))