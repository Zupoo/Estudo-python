# CRUD
# R
# READ

import pyodbc

print(pyodbc.drivers())

caminho_Database = r"C:\Users\Zupo\Desktop\estudo\27 SQL\chinook.db"

dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"
                 f"Database={caminho_Database}")

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

#lendo informaçoes da tabela custumers do chinook

cursor.execute("SELECT * FROM customers")

valores = cursor.fetchall()

for item in valores:
    print(item)
    print('-'*20)



cursor.close()
conexao.close()


