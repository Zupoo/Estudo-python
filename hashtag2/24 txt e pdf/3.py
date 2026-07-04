# Estrutura with é usada pra abrir e fechar alguma coisa automaticamente
#da no mesmo , só muda que n precisa fazer o .close()
# mas a "variavel" criada dentro dro with só funciona no with
with open('Contagem100.txt', 'w') as txt:
    for i in range(100):
        txt.write(f'{i+1}\n')
