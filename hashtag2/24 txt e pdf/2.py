# ao usar o W ele cria um novo arquivo, caso o arquivo ja exista ele vai substituir
#ao usar o A se o arquivo ja existir ele vai só adicionar
# .write() é o metodo para escrever no arquivo
# sempre q usar o open deve ser usado o metodo close() tb

novo_txt = open('Primeiro.txt', 'w')
novo_txt.write('Olá mundo!!! \ncontra barra N pra pular linha\n')
novo_txt.write('Usar outro o ')
novo_txt.write('metodo write() dnv não funciona para pular linha\n')
novo_txt.write('Vou fazer um for pra testar\n')
for i in range (101):
    novo_txt.write(f'{i}\n')
novo_txt.close()
