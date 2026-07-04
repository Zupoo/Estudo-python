import PyPDF2 as pyf
from pathlib import Path #importar a biblioteca path para salvar os pdfs

#atribuindo o local do pdf na variavel nome
nome = r"C:\Users\Zupo\Desktop\estudo\24 txt e pdf\MGLU_ER_3T20_POR (1).pdf"

# lendo o pdf e salvando ele na variavel arquivo_pdf
arquivo_pdf = pyf.PdfReader(nome)
local = r"C:\Users\Zupo\Desktop\estudo\24 txt e pdf\paginas"


print(len(arquivo_pdf.pages)) #.pages cria uma lista com as paginas do pdf



novo_pdf = pyf.PdfWriter() #crio uma variavel do tipo escrever pdf
novo_pdf.add_page(arquivo_pdf.pages[13]) # coloco o a pagina dentro da minha variavel
arquivo =  Path(f"Teste_Arquivo_Pagina_14.pdf").open(mode="wb")
novo_pdf.write(arquivo) 
arquivo.close()
        



