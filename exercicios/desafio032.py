import datetime
ano = int(input('Digite o ano q voce gostaria de saber se é bissexto , caso queira saber o ano atual digite 0 : '))
if ano == 0:
    ano = datetime.date.today().year
if ano%4 == 0 and ano %100 != 0 or ano%400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} NÃO é bissexxto'.format(ano))
