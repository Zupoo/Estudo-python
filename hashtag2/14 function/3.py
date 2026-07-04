# função passando parametros
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

def somar(num1, num2):
    return num1 + num2

soma = somar(n1, n2)
print(soma)