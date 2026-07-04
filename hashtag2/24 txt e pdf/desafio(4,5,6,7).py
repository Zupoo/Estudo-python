
def gerador_txt (nome_arquivo, lista):
    #adiciona itens de uma lista em um aquivo txt
    nome_arquivo_txt = nome_arquivo + '.txt'
    txt = open(nome_arquivo_txt, 'w')
    for item in lista:
        txt.write(item)
    txt.close()            

alunos_organicos = []
alunos_nao_organicos = []
lixo = []
alunos = open(r'C:\Users\Zupo\Desktop\estudo\24 txt e pdf\Alunos.txt', 'r')

#percorrendo todo o txt, encontrando alunos com _org_ e adicionando eles na lista alunos_organicos
for linha in alunos.readlines():
    if '_org_' in linha:
        alunos_organicos.append(linha)
    elif '@' in linha:
        alunos_nao_organicos.append(linha)
    else:
        lixo.append(linha)


gerador_txt('alunos_organicos',alunos_organicos ) #criando um txt com todos os alunos organicos
gerador_txt('alunos_nao_organicos', alunos_nao_organicos)
gerador_txt('lixo', lixo)

org_yt = []
org_fb = []
org_ig = []
for aluno in alunos_organicos:
    if '_yt_' in aluno:
        org_yt.append(aluno)
    if '_fb_' in aluno:
        org_fb.append(aluno)
    if '_ig_' in aluno:
        org_ig.append(aluno) 

gerador_txt('yt', org_yt)


alunos.close()