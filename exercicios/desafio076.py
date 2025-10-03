# tupla = 'Lápis', 1.75, 'Caneta', 2.50, 'Caderno', 15.30, 'Borracha', 3.20, 'Marcador', 5.00, 'Tesoura', 7.40, 'Régua', 4.10, 'Apontador', 2.00, 'Papel A4', 10.00, 'Pasta de arquivo', 12.60

# print(f'''
# {tupla[0]:.<30} {tupla[1]}
# {tupla[2]:.<30} {tupla[3]}
# {tupla[4]:.<30} {tupla[5]}
# {tupla[6]:.<30} {tupla[7]}
# {tupla[8]:.<30} {tupla[9]}
# {tupla[10]:.<30} {tupla[11]}
# {tupla[12]:.<30} {tupla[13]}
# {tupla[14]:.<30} {tupla[15]}
# {tupla[16]:.<30} {tupla[17]}
# {tupla[18]:.<30} {tupla[19]}
# ''')
j = 0
tupla = 'Lápis', 1.75, 'Caneta', 2.50, 'Caderno', 15.30, 'Borracha', 3.20, 'Marcador', 5.00, 'Tesoura', 7.40, 'Régua', 4.10, 'Apontador', 2.00, 'Papel A4', 10.00, 'Pasta de arquivo', 12.60
for c in range(0,len(tupla)//2):
    print(f'''
    {tupla[j]:.<30} R${tupla[j+1]:.2f}
    ''')
    j = j + 2
