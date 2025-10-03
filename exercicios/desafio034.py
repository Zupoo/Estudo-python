salario = float(input('Qual o salário?: '))

if salario > 1250:
    aumento = salario * 0.1
    novosalario = salario + aumento
else:
    aumento = salario * 0.15
    novosalario = salario + aumento
print ('O seu salario teve um aumento de {:.2f} R$ e passou de {:.2f} R$ para {:.2f} R$.'.format(aumento, salario, novosalario))