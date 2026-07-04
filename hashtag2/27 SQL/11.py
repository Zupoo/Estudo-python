import pyodbc
import pandas as pd
# print(pyodbc.drivers())
caminho_database = r"C:\Users\Zupo\Desktop\estudo\27 SQL\salarios.sqlite"
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"
                 f"Database={caminho_database}")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

#VOU DELETER O ID 3 DA TABELA ALBUNS
cursor.execute('''
SELECT * FROM Salaries
               ''')

valores = cursor.fetchall()
description = cursor.description #pegando o description para pegar o nome das colunas

colunas = [] #criando uma lista pra depois receber o nome das colunas
 
for tupla in description: #percorrendo o desciption pra pegar o nome de cada coluna, o description é uma tupla com varias tuplas,
                             # e o nome das colunas é o primeiro item de cada tupla
    colunas.append(tupla[0])


tabela_salarios = pd.DataFrame.from_records(valores[:10], columns=colunas)

print(tabela_salarios.to_string())


cursor.close()
conexao.close()