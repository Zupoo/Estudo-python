#lambda expressions
# é um afuncao anonima
# é usada quando voce quer fazer uma funcao q executa só uma linha de codigo
# por exemplo uma funcao q n tem nada dentro, só um return
# ex : 
def soma_um (n):
    return n + 1
print(soma_um(10))
# a lambda expression tem esse formato
# nome_da_funcao = lambda parametros: expressao
mais_um = lambda n: n + 1
print(mais_um(10))