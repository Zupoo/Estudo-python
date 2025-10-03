n = int(input('Digite um numero : '))
cont = 1
soma = n
maior = n
menor = n
continuar = input('Quer continuar e digitar mais um numero? responda [SIM] ou [NAO]').upper().strip()
while continuar == 'SIM':
    n = int(input('Entao digite outro numero'))
    cont = cont + 1
    soma = soma + n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    print(soma , cont)
    continuar = input('Quer continuar e digitar mais um numero? responda [SIM] ou [NAO]: ').upper().strip()
    while continuar != 'SIM' and continuar != 'NAO':
        continuar = input('Não entendi se voce deseja ou nao continuar , digite SIM para continuar ou NAO para parar').upper().strip()

media = soma / cont
print(media)
print(maior, menor)

