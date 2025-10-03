print('-'*30)
peso = float(input('Qual o seu peso? : '))
alturacm = float(input('Qual a sua altura? (Em cm): '))
print('-'*20)
alturam = alturacm /100
imc = peso / (alturam * alturam)
ideal = 0
if imc < 18.5:
    print('Seu IMC é de {:.2f} e isso quer dizer q voce esta Abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    ideal = 1
    print('Seu IMC é de {:.2f} e isso quer dizer q voce esta no Peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é de {:.2f} e isso quer dizer q voce esta com Sobre peso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.2f} e isso quer dizer q voce esta com Obesidade'.format(imc))
else:
    print('Seu IMC é de {:.2f} e isso quer dizer q voce esta com Obesidade mórbida'.format(imc))

if ideal != 1:
    pesoideal1 = 24.99* (alturam * alturam)
    pesoideal2 = 18.5 * (alturam * alturam)
    print('Voce deveria ter entre {:.1f}kg e {:.1f}kg para estar no peso ideal'.format(pesoideal1, pesoideal2))
