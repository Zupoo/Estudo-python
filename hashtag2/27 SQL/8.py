# import pyodbc
# print(pyodbc.drivers())
# caminho_database = r"C:\Users\Zupo\Desktop\estudo\27 SQL\chinook.db"
# dados_conexao = ("Driver={SQLite3 ODBC Driver};"
#                  "Server=localhost;"
#                  f"Database={caminho_database};")
# conexao = pyodbc.connect(dados_conexao)
# cursor = conexao.cursor()
#NESSA AULA VOU APRENDER A COMO FAZER A MESMA COISA Q A AULA 7 (READ) SÓ QUE COM O PANDAS EM VEZ DE COM O PYODBC
import pandas as pd
import sqlite3 #precisa usar essa biblioteca pra isso, ela ja vem instalada no python

conexao = sqlite3.connect(r"C:\Users\Zupo\Desktop\estudo\27 SQL\chinook.db")


# tabela_clientes = pd.read_sql("COMANDO SQL", conexao)
tabela_clientes = pd.read_sql("SELECT * FROM customers", conexao)
print(tabela_clientes)

conexao.close()