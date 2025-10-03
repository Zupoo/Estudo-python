import pandas as pd
#importando os arquivos
vendas_df = pd.read_csv(r'modulo22\Contoso - Vendas - 2017.csv', sep=';', encoding='latin1')
produtos_df = pd.read_csv(r'modulo22\Contoso - Cadastro Produtos.csv', sep=';', encoding='latin1')
lojas_df = pd.read_csv(r'modulo22\Contoso - Lojas.csv', sep=';', encoding='latin1')
clientes_df = pd.read_csv(r'modulo22\Contoso - Clientes.csv', sep=';', encoding='latin1')

clientes_df = clientes_df.rename(columns={'ÿID Cliente' : 'ID Cliente'})
produtos_df = produtos_df.rename(columns={'ÿNome do Produto' : 'Nome do Produto'})
lojas_df = lojas_df.rename(columns={'ÿID Loja' : 'ID Loja'})

#limpando apenas as colunas que queremos
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

#mesclando e renomeando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})

print(vendas_df.columns)

contoso = vendas_df[(vendas_df['Nome da Loja'] == 'Loja Contoso Europe Online ') & (vendas_df['Quantidade Devolvida'] == 0)]
# contoso_sem_vendidos = vendas_df[contoso & sem_vendidos]
# contoso = vendas_df['ID Loja'] == 306
# loja_contoso = vendas_df[contoso]
# loja_contoso_sem_devolvido = loja_contoso['Quantidade Devolvida'] == 0
# print(loja_contoso)
# print(loja_contoso.columns)
print(contoso)