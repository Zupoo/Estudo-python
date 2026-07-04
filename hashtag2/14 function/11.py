# função q retorna mais de um valor
def calculos(n1, n2):
    soma= n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2
    return soma, subtracao, multiplicacao, divisao

print(calculos(7, 2))