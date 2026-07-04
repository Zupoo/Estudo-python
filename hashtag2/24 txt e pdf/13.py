#adicionar uma parina no meio só fazer igual ao 12.2 mas usar o .merge(posicao, arquivo)


import PyPDF2 as pyf
from pathlib import Path #importar a biblioteca path para salvar os pdfs

pdf_mesclado = pyf.PdfMerger()

pdf_mesclado.append(r"C:\Users\Zupo\Desktop\estudo\24 txt e pdf\MGLU_ER_4T20_POR (1).pdf")
pdf_mesclado.merge(1, r"C:\Users\Zupo\Desktop\estudo\24 txt e pdf\paginas\Arquivo_Pagina_1.pdf")

local = r"C:\Users\Zupo\Desktop\estudo\24 txt e pdf\paginas" #aonde eu quero salvar o o arquivo , é mais facil colocar em uma variavel pra passar como parametro no path
with Path(local, f"pdf_mesclado_com_o_merge.pdf").open(mode="wb") as arquivo: #crio um arquivo com o nome, abro ele como "wb" que quer dizer q é write alguam coisa(escrever) , o primeiro parametro é o caminhao, o segundo é o nome do arquivo
    pdf_mesclado.write(arquivo)  #essa parte é meio invertida mas blz, na minha cabeça era pra ser ao contrario 

