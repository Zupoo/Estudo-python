arquivo = open('modulo25/txt/Alunos.txt', 'r')
# arquivo_novo = open('Novo', 'w')
linhas = arquivo.readlines()
del linhas[:4]
contsite = contyt = contig = contigfb = contanuncio = cont = organico = 0
for linha in linhas:
    cont = cont + 1
    email, origem = linha.split(',')
    if 'hashtag_site_org' in origem or 'hashtag_yt_org' in origem or 'hashtag_ig_org' in origem or 'hashtag_igfb_org' in origem or '_org' in origem:
        organico = organico + 1
        if 'hashtag_site_org' in origem:
            contsite = contsite + 1
        if 'hashtag_yt_org' in origem:
            contyt = contyt + 1
        if 'hashtag_ig_org' in origem:
            contig = contig + 1
        if 'hashtag_igfb_org' in origem:
            contigfb = contigfb + 1
    else:
        contanuncio = contanuncio + 1
lista = [contsite, contyt, contig, contigfb]
maior = max(lista)
with open('exercicio1.txt', 'w') as exercicio1:
    exercicio1.write(f'Total de alunos orgânicos: {organico}\n')
    exercicio1.write(f'Alunos orgânicos pelo site {contsite}\n')
    exercicio1.write(f'Alunos orgânicos pelo youtube {contyt}\n')
    exercicio1.write(f'Alunos orgânicos pelo instagram {contig}\n')
    exercicio1.write(f'Alunos orgânicos pelo facebook {contigfb}\n')
    exercicio1.write(f'Dos {cont} alunos analisados {organico} vieram do organico e {contanuncio} vieram do anuncios\n')
    exercicio1.write(f'A melhor fonte organica é o youtube com {contyt} novo alunos\n')

print('Arquivo exercicio1.txt criado')
