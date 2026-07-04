#a conexão é feita em 3 etapas
# as 2 primeiras sao configurações a terceira etapa é execução do comando


# levando em conta que ja esta com os drivers instalados e a biblioteca do pyodbc

# etapa 1
import pyodbc

# dados_conexao = ("Driver={é aquele la do print(pyodbc.drivers()) , tem q ser entre chaves};Server=depende, pode ser um link ou algo assim, é aonde esta o banco de dados, no caso por agora vai ser localhost pq esta no meu computador;Database=é o nome do banco de dados")
caminho_banco = r"C:\Users\Zupo\Desktop\estudo\27 SQL\salarios.sqlite"
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"
                 f"Database={caminho_banco}")
conexao = pyodbc.connect(dados_conexao)
print("conexão bem sucedida")

# etapa 2
# criar um cursor
# cursor é oq usamos o tempo todo pra executar os comandos sql.
cursor = conexao.cursor()


# etapa 3
# executar a ação 

# #eu tava conectando errado(PRECISAVA DO CAMINHO PQ ESTOU ABRINDO A PASTA ESTUDO E NAO A PASTA SQL)
#e pedi ajuda pra IA , ela me mostrou isso aqui para ver quais tabelas tem no banco q eu estou conectado
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tabelas = cursor.fetchall()
# print("Tabelas disponíveis:", tabelas)

# cursor.execute("SELECT * FROM nome_da_tabela")
cursor.execute("SELECT * FROM Salaries")
valores = cursor.fetchall()  #joga tudo q esta no cursor na variavel valores
print(valores[:3])

#sempre tem finalizar o cursor e a conexao
cursor.close()
conexao.close