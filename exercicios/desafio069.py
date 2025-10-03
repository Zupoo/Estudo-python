dezoito = 0
homens = 0
mulheresmenos20 = 0
total = 0
while True:
    print('Cadastre uma pessoa')
    idade = int(input('Idade : '))
    while True:
        sexo = input('Sexo: [M/F] : ').strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
    while True:
        continuar = input('Quer continuar? [S/N]').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
    if idade >= 18 :
        dezoito = dezoito +1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 = mulheresmenos20 + 1
    total = total + 1
    if continuar == 'N':
        break
print(f'Foram cadastradas {total} pessoas , Dessas {dezoito} sao de maior , Foram cadastrados {homens} homens e {mulheresmenos20} mulheres com menos de 20 anos')
