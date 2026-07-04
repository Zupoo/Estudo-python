#juntando pdfs
#neste exercicio vou juntar as paginas q separei no passado

import PyPDF2 as pyf
from pathlib import Path #importar a biblioteca path para salvar os pdfs

paginas_escolhidas = [1, 10, 14] #vou juntar esses 3 paginas(que na verdade sao 3 arquivos q foram separados antes)

pdf_junto = pyf.PdfWriter() #criando a variavel do tipo pyf.writer() pra ela receber os pdfs

for pagina in paginas_escolhidas: #um for pra percorrer a lista das paginas q eu qeuro e conseguir substituir no nome do arqquivo
    pdf = pyf.PdfReader(rf'C:\Users\Zupo\Desktop\estudo\24 txt e pdf\paginas\Arquivo_Pagina_{pagina}.pdf') #lendo e salvando na variavel pdf o pdf lido
    pdf_junto.add_page(pdf.pages[0]) #adicionando na variavel pdf_junto o arquivo q acabei de le e salvar na veriavel pdf na linha de cima (precisa ter essa [0])


#salvar
local = r"C:\Users\Zupo\Desktop\estudo\24 txt e pdf\paginas" #aonde eu quero salvar o o arquivo , é mais facil colocar em uma variavel pra passar como parametro no path
with Path(local, f"Paginas_escolhidas.pdf").open(mode="wb") as arquivo: #crio um arquivo com o nome, abro ele como "wb" que quer dizer q é write alguam coisa(escrever) , o primeiro parametro é o caminhao, o segundo é o nome do arquivo
    pdf_junto.write(arquivo)  #essa parte é meio invertida mas blz, na minha cabeça era pra ser ao contrario 

