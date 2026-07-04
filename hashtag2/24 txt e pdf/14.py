import PyPDF2 as pyf
from pathlib import Path #importar a biblioteca path para salvar os pdfs


nome = r"C:\Users\Zupo\Desktop\estudo\24 txt e pdf\MGLU_ER_3T20_POR (1).pdf"    #local aonde esta salvo o pdf
arquivo_pdf = pyf.PdfReader(nome)   #lendo o pdf e salvando na variavel arquivo_pdf

metadados_arquivo = arquivo_pdf.metadata    #apenas demonstrando como pegar algumas informaçoes do arquivo com o .metadados
print(metadados_arquivo)

texto_referencia = "| Despesas com Vendas "  #o q nos estamos "procurando"
for i, pagina in enumerate(arquivo_pdf.pages):  #um for pra percorrer cada pagina do pdf
    texto_pagina = pagina.extract_text()  #colocando o texto de cada pagina na variavel texto_pagina
    if texto_referencia in texto_pagina: # se tiver o texto referencia(o que nos estamos procurando) nessa variavel texto_pagina
        print("Numero Pagina: ", i+1)  
        texto_analisar = texto_pagina #coloco o texto todo nessa variavel texto_analisar

print(texto_analisar)   

#agora que encontramos em qual pagina esta o q eu quero
#vamos pegar só o pedaço 
posicao_inicial = texto_analisar.find(texto_referencia) #aonde começa oq eu quero
posicao_final = texto_analisar.find("|", posicao_inicial + 1) #aonde termina o segundo parametro q passa nesse .find é :a partir de onde começar a procurar

texto_final = texto_analisar[posicao_inicial:posicao_final]   
print(texto_final)