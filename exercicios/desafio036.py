casa = float(input('Qual o valor a casa? : '))
salario = float(input('Qual o seu salário? : '))
anos = float(input('Em quantos anos voce pretende pagar: : '))

prestação = casa / (anos*12)
# print('Prestação salario preçocasa anos',prestação, salario, casa, anos)

if prestação > salario*0.3:
    salariominimo = prestação / 0.3
    print('Imprestimo negado , o valor da prestação mensal excede o limite de 30% do saliario mensal')
    print('Prestação mensal = {:.2f} \nSalario mensal {:.2f}\n'.format(prestação, salario))
    print('O salario deveria ser de no minimo {:.2f}R$ para ser possivel retirar o emprestimo e pagar a casa em {:.0f} anos'.format(salariominimo, anos))
elif prestação <= salario * 0.3:
    print('Parabens voce pode fazer seu emprestimo')
    print('A prestação mensal vai ser de {:.2f}R$'.format(prestação))
else:
    print('Acho q voce digitou algo errado')