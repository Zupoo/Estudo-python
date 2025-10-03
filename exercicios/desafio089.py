# lista = []
# listinha = []
# listinhazinha = []
# continuar = ''
# cont = 0
# while True:
#     listinha.append((input('Nome : ')))
#     listinhazinha.append(float(input('Nota 1 : ')))
#     listinhazinha.append(float(input('Nota 2 : ')))
#     listinha.append(listinhazinha[:])
#     media = (listinhazinha[0] + listinhazinha[1])/2
#     listinha.append(media)
#     lista.append(listinha[:])
#     listinha.clear()
#     listinhazinha.clear()
#     while continuar != 'S' and continuar != 'N':
#         continuar = input('Quer cadastrar mais alunos?[S/N] : ').strip().upper()
#     if continuar == 'N':
#         break
#     continuar = 0
# for c , aluno in enumerate(lista):
#     print(f'Numero:{c} / Aluno: {aluno[0]}{' ':-<7} / Média: {aluno[2]}')
# print('-='*33)
# while True:
#     gostaria = input('Gostaria de ve as notas de algum dos alunos?[S/N] : ').strip().upper()
#     print('-='*33)
#     if gostaria == 'N':
#         break
#     else:
#         n = int(input('Qual o numero do aluno q voce gostaria de saber as notas? : '))
#     print('-='*33)
#     print(f'Aqui estao as notas do {lista[n][0]} : Nota 1 {lista[n][1][0]} Nota 2 {lista[n][1][1]}')
#     print('-='*33)


lista = []
continuar = ''
cont = 0
while True:
    nome = (input('Nome : '))
    nota1 = float(input('Nota 1 : '))
    nota2 = float(input('Nota 2 : '))
    media = (nota1 + nota2)/2
    lista.append([nome, [nota1, nota2], media])
    print(lista)
    while continuar != 'S' and continuar != 'N':
        continuar = input('Quer cadastrar mais alunos?[S/N] : ').strip().upper()
    if continuar == 'N':
        break
    continuar = 0
for c , aluno in enumerate(lista):
    print(f'Numero:{c} / Aluno: {aluno[0]}{' ':-<7} / Média: {aluno[2]}')
print('-='*33)
while True:
    gostaria = input('Gostaria de ve as notas de algum dos alunos?[S/N] : ').strip().upper()
    print('-='*33)
    if gostaria == 'N':
        break
    else:
        n = int(input('Qual o numero do aluno q voce gostaria de saber as notas? : '))
    print('-='*33)
    if n >= 0 and n < len(lista):
        print(f'Aqui estao as notas do {lista[n][0]} : Nota 1 {lista[n][1][0]} Nota 2 {lista[n][1][1]}')
        print('-='*33)
