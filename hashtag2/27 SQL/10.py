# CRUD
# DELETE
import pyodbc
print(pyodbc.drivers())
caminho_database = r"C:\Users\Zupo\Desktop\estudo\27 SQL\chinook.db"
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"
                 f"Database={caminho_database}")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

#VOU DELETER O ID 3 DA TABELA ALBUNS
cursor.execute('''
DELETE FROM albums WHERE AlbumId=3
               ''')
cursor.commit()


                




cursor.close()
conexao.close()