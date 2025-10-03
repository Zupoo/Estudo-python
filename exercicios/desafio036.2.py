#quanto tem q ser meu salario pra eu conseguir alugar uma casa?
#a mensalidade deve ser no maximo 30% do salario
#caso a mensalidade for maior q 30% do salario
#quanto eu devo ganhar pra poder pegar o imprestimo?

salario = float(input('Informe o seu salario'))
mensalidade = float(input('Informe a mensalidade'))
if mensalidade <= salario * 0.3:  #se a mensalidade for menor q o salario
    print(' voce pode alugar a casa')
    print('A mensalidade é menor q 30% do seu salario')
    print('30% do seu salario é maior q a mensalidade')
elif mensalidade > salario * 0.3:
    print('voce nao pode pagar pelo imprestimo')
    minimo = mensalidade / 0.3
    print('O seu salario tem q ser pelo menos {}'.format(minimo))