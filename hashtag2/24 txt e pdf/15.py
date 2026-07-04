#aprendendo a usar o tabula
#ele é usado para extrair tabelas de pdf
#pra instalar ele é pip intall tabula-py  (NAO É SÓ TABULA, É TABULA -PY)
#tb precisa ter o java instalado para ele funcionar

import tabula
from IPython.display import display

nome = r"C:\Users\Zupo\Desktop\estudo\24 txt e pdf\MGLU_ER_3T20_POR (1).pdf"    #local aonde esta salvo o pdf

tabelas = tabula.read_pdf(nome, pages=5) #coloca na variavel tabelas todas as tabelas da pagina 5
df_resultado = tabelas[0] #pega só a tabela [0] de tabelas e coloca em df_resultado

#excluir linhas totalmente vazias
df_resultado = df_resultado.dropna(how="all", axis=0) #o dropna é usado para excluir linhas de uma df , passa 2 parametros pro .dropna, sao eles: how -> como ele vai analisar (all quer dizer que é só se tiver todas as linhas vazias, any para pelo menos 1 valor vazio)e axis -> o eixo , 0 pra linhas e 1 pra colunas
#excluir colunas totalmente vazias
df_resultado = df_resultado.dropna(how="all", axis=1)

#tornando a primeira linha de uma tabela um cabeçalho
df_resultado.columns = df_resultado.iloc[0]   #esta definindo q a linha 1 vai ser o cabeçalho

df_resultado = df_resultado.iloc[1:] #"cortando" a linha 1 da tabela pq agora ela é cabeçalho entao n deve aparecer ela 2x

df_resultado = df_resultado.reset_index(drop=True) #resetando o index (a contagem) se nao colocar esse drop=True os indices antigos vao virar uma nova coluna na df

print(df_resultado)
