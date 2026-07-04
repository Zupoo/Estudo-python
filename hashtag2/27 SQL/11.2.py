import sqlite3
import pandas as pd

caminho_database =  r"C:\Users\Zupo\Desktop\estudo\27 SQL\salarios.sqlite"
with sqlite3.connect(caminho_database) as conexao:

    tabela_salarios = pd.read_sql("SELECT * FROM Salaries", conexao)
    print(tabela_salarios)
