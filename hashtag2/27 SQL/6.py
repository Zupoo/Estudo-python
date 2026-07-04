# CRUD
# CREATE
import pyodbc
print(pyodbc.drivers())

# CONEXAO É PADRAO , SÓ MUDA O DRIVER SERVER E O DATABASE
caminho_Database = r"C:\Users\Zupo\Desktop\estudo\27 SQL\chinook.db"
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"
                 f"Database={caminho_Database}")

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

#todo comando que faça alguma alteração no banco de dados depois dele tem q fazer um commit cursor.commit()
#adicionando uma alguma coisa na tabela albuns do chinook
cursor.execute("""
INSERT INTO albums (Title, ArtistId)
VALUES
('Zupo', 67)               
""")
cursor.commit()


#fechar o cursor e o a conexao
cursor.close()
conexao.close()