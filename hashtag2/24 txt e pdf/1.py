#abrir arquivo txt
#usamos 'r' para abrir o arquivo para ler (read) e 'w' quando abrimos o arquivo para escrever (write)
# usamos 'a' se formaos adicionar (append) uma informação no arquivo 
# ao usar o W ele cria um novo arquivo, caso o arquivo ja exista ele vai substituir
#ao usar o A se o arquivo ja existir ele vai só adicionar
arquivo = open(r'C:\Users\Zupo\Desktop\estudo\24 txt e pdf\Alunos.txt', 'r')


# o read() só printa
print(arquivo.read())
# o readlines printa e transforma cada linha em uma lista
print(arquivo.readlines())