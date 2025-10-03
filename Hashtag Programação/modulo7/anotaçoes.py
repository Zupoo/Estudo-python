email = 'gui.tijuca@gmail.com'
#tamanho do email 
print(len(email))

#primeira letra
print(email[0])

# numeros negativos pra pegar de tras pra frente
print(email[-1])

#quando tem .algumacoisa() é um metedo e oq esta dentro do () é chamado de argumento
#todos os metodos estao no arquivo módulo_string nessa pasta

print(email.endswith('gmail.com'))
texto = email.find('gmail.com')
print(texto)

#alinhamento :>   :<    :^ 
print(f'Meu email é {email :<30} sei la alguma coisa')
print(f'Meu email é {email :>30} sei la alguma coisa')
print(f'Meu email é {email :^30} sei la alguma coisa')
numerao = 1000000
print(f'Toma ai o numerao {numerao}')
print(f'Toma ai o numerao {numerao :,}')
