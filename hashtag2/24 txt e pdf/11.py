import PyPDF2 as pyf
from pathlib import Path #importar a biblioteca path para salvar os pdfs

#atribuindo o local do pdf na variavel nome
nome = r"C:\Users\Zupo\Desktop\estudo\24 txt e pdf\MGLU_ER_3T20_POR (1).pdf"

# lendo o pdf e salvando ele na variavel arquivo_pdf
arquivo_pdf = pyf.PdfReader(nome)


print(len(arquivo_pdf.pages)) #.pages cria uma lista com as paginas do pdf


local = r"C:\Users\Zupo\Desktop\estudo\24 txt e pdf\paginas"
for i, pagina in enumerate(arquivo_pdf.pages):
    num_pagina = i + 1
    novo_pdf = pyf.PdfWriter() #crio uma variavel do tipo escrever pdf
    novo_pdf.add_page(pagina) # coloco o a pagina dentro da minha variavel
    with Path(local, f"Arquivo_Pagina_{num_pagina}.pdf").open(mode="wb") as arquivo: #crio um arquivo com o nome, abro ele como "wb" que quer dizer q é write alguam coisa(escrever)
        novo_pdf.write(arquivo) 

        



