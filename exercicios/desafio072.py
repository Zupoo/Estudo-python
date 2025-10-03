while True:
    numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    while True:
        n = int(input('Digite o numero entre 0 e 20 q voce quer ve escrito por extenso : '))
        if n >= 0 and n <=20:
            break
    print(numeros[n])
    while True:
        continuar = input('Voce quer continuar? [S/N] : ').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
    # continuar = ''
    # while continuar != 'S' and continuar != 'N':
    #     continuar = input('Voce quer continuar? [S/N] : ').strip().upper()
    if continuar == 'N':
        break
print('FIM')

