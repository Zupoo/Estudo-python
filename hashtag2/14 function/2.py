# função que retorna algo

# estrutura basica
# def nome_funcao():
#     codigocodigocodigo
#     codigo
#     codigocodigocodigo
#     codigo
#     return oq_quiser_retornar


def somar():
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero'))
    return n1 + n2

soma = somar()
print(f'a soma é {soma}')