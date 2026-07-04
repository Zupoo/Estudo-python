# CRUD
# UPDATE
import pyodbc
print(pyodbc.drivers())
caminho_database = r"C:\Users\Zupo\Desktop\estudo\27 SQL\chinook.db"
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"
                 f"Database={caminho_database};")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

#VOU ALTERAR A TABELA CUSTOMERS, ALTERAR O EMAIL DO LUIS, O PRIMEIRO DA TABELA
cursor.execute('''
UPDATE customers SET Email="Robson@robson.robson" WHERE CustomerId="1"
''')
cursor.commit()


cursor.close()
conexao.close()