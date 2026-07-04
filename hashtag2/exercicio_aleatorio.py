def cripto(palavra):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    criptografada = []
    for letra in palavra:
        criptografada.append(alfabeto.index(letra)+1)
    return criptografada            
    
    
palavra = input('Digite a palavra que vai ser criptografada: ')
palavra_criptografada = cripto(palavra)
print(palavra_criptografada)
