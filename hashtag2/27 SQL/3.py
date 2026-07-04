# instalar o pyodbc
# é a biblioteca q é usada para integrar o python com o banco de dados
#pra testar se baixou direito é só importar e rodar pra ve se ta tudo certo
import pyodbc

print(pyodbc.drivers())   #é usado para ve quais drivers tem instalado
# se no print nao aparecer esses  'SQLite3 ODBC Driver', 'SQLite ODBC Driver', 'SQLite ODBC (UTF-8) Driver']
# aqui esta o link de instalação do driver
# https://www.ch-werner.de/sqliteodbc/

